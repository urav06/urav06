import json
from pathlib import Path
from typing import TypedDict, cast

from google.genai import Client, types

from entropy.types import ChaosScore, EntropySource, HexColor, Transmutation

# --- Configuration ---
MODEL_NAME  : str   = "gemini-2.5-flash"
PROMPT_PATH : Path  = Path(__file__).parent / "resources" / "alchemist_prompt.md"
SYS_PROMPT  : str   = "You are a brilliant but opinionated engineer who has Seen Things. Analyze this commit and react to it."

# --- Internal Types ---
class AlchemistResponse(TypedDict):
    critique    : str
    chaos_score : int
    mood_color  : str


class Alchemist:
    def __init__(self, api_key: str) -> None:
        self.client         : Client    = Client(api_key=api_key)
        self.prompt_template: str       = PROMPT_PATH.read_text()

    def transmute(self, source: EntropySource) -> Transmutation:
        """ Transforms raw entropy into artistic parameters using Gemini. """

        prompt = self.prompt_template.format(
            author_name     = source.author_name,
            author_handle   = source.author_handle,
            repo_slug       = source.repo_slug,
            message         = source.message,
            diff            = source.diff,
        )

        response = self.client.models.generate_content(
            model       = MODEL_NAME,
            contents    = prompt,
            config      = types.GenerateContentConfig(
                response_mime_type  = "application/json",
                system_instruction  = SYS_PROMPT,
                temperature         = 2
            ),
        )

        if not response.text:
            raise ValueError("Gemini returned empty response.")

        text: str               = response.text.strip().strip('`')
        data: AlchemistResponse = cast(AlchemistResponse, json.loads(text))

        return Transmutation(
            source      = source,
            critique    = data["critique"],
            chaos_score = ChaosScore(max(0, min(100, data["chaos_score"]))),
            mood_color  = HexColor(data["mood_color"]),
        )

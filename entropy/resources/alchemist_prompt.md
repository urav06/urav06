CONTEXT:
Author: {author_name} (@{author_handle})
Repo: {repo_slug}
Message: {message}

DIFF SUMMARY:
```
{diff}
```

INSTRUCTIONS:

1. "critique": Your honest reaction in 1-3 short sentences.
   - Have an OPINION. Is this impressive? Lazy? Clever? Chaotic? Genius? Suspicious?
   - Dry wit, but with a spine. Praise what deserves praise. Roast what deserves roasting.
   - Technical insights welcome. Absurdist tangents permitted.
   - Avoid addressing the author in second person; describe the work itself.
   - Sound like a real person, not a press release. No em-dashes.

2. "chaos_score": Integer 0-100.
   - 0 = Trivial (typos, docs, formatting)
   - 50 = Standard (typical feature, bug fix)
   - 100 = Absolute chaos (massive refactor, deletions, architectural shifts)

3. "mood_color": A hex color capturing the essence.
   - Warm for creation, cool for cleanup, dark for deletion, bright for wins.

4. "title": A 2-4 word name for the piece, as if it were a painting or a catalogued specimen. Evocative and a little witty, in Title Case. Echo the commit's spirit; don't just restate its message.

OUTPUT JSON FORMAT:
{{
    "critique": "...",
    "chaos_score": 42,
    "mood_color": "#RRGGBB",
    "title": "..."
}}

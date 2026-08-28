### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1787928933" alt="Entropy" width="365">

### The Bot's Planning Deck

Chaos ░░░░░░░░░░ 5 · Mood $\color{#8BC34A}{\blacksquare}$ #8BC34A

[github/spec-kit](https://github.com/github/spec-kit) by [@github-actions[bot]](https://github.com/github-actions[bot]) · [`241eaca`](https://github.com/github/spec-kit/commit/241eaca090655b9fb4349696b1d619e78bd16db9)

~~~
Add Pre-Spec Cards extension to community catalog (#4365)

Add prespec extension submitted by @bendlikeabamboo to:
- extensions/catalog.community.json (alphabetical order)
- docs/community/extensions.md community extensions table

…
~~~

A bot, with Copilot's thoughtful assistance, dutifully catalogs a new 'pre-spec' ideation tool. Formalizing the messy 'before the spec' phase is genius; that's where chaos typically breeds. And yes, those futuristic timestamps really seal the deal on confidence.

<sub>captured 2026-08-28</sub>

</div>
<!-- ENTROPY:END -->

---

<details>
<summary>What is this?</summary>

<br>

```mermaid
flowchart LR
    commit["🌌 daily commit"] -->|diff| gemini["Gemini"]
    gemini -->|chaos + mood| attractor["Lorenz attractor"]
    gemini -->|title + roast| exhibit["today's exhibit"]
    attractor --> exhibit
```

A GitHub Action runs daily and picks a commit: mine if I've pushed recently, otherwise something from my network or a starred repo, and the Linux genesis commit as a last resort. Gemini gives it a name, a roast, a chaos score (0-100), and a mood color. Those become a [Lorenz attractor](https://en.wikipedia.org/wiki/Lorenz_system): chaos controls how wild the butterfly gets, mood tints the gradient, and the commit hash sets the starting point. The math is identical every run, so the commit is the only thing that changes the picture.

[See the code →](./entropy)

</details>
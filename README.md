### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1788507869" alt="Entropy" width="365">

### Bot's Descriptive Update

Chaos █░░░░░░░░░ 15 · Mood $\color{#4CAF50}{\blacksquare}$ #4CAF50

[github/spec-kit](https://github.com/github/spec-kit) by [@github-actions[bot]](https://github.com/github-actions[bot]) · [`df6b318`](https://github.com/github/spec-kit/commit/df6b3187022ce986759bd854467e8a4bb56bb0f4)

~~~
Update Linear Integration extension to v0.8.0 (#4428)

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>
~~~

A bot, dutifully updated by another bot, for an integration that promises *automatic mirroring* of specs. It's bots all the way down. At least the description actually tells me what it does now, rather than technical jargon; a good documentation improvement is always appreciated, even if it's bot-generated boilerplate.

<sub>captured 2026-09-04</sub>

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
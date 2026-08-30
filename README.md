### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1788080199" alt="Entropy" width="365">

### Foundational Paradox

Chaos ░░░░░░░░░░ 0 · Mood $\color{#FFB14A}{\blacksquare}$ #FFB14A

[urav06/ship-of-theseus](https://github.com/urav06/ship-of-theseus) by [@urav06](https://github.com/urav06) · [`0486878`](https://github.com/urav06/ship-of-theseus/commit/04868789ce426e2f74e4c5fdcbe4cf99fd18594c)

~~~
Initial commit
~~~

An initial commit that courageously plants a flag in the future with its copyright year, while instantly encapsulating its namesake paradox in a witty README. It's an empty, licensed vessel, conceptually intriguing before a single line of logic exists.

<sub>captured 2026-08-30</sub>

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
### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1787456982" alt="Entropy" width="365">

### The Padded Peace

Chaos ██████░░░░ 65 · Mood $\color{#2E8BC0}{\blacksquare}$ #2E8BC0

[palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) by [@htin1](https://github.com/htin1) · [`3026f72`](https://github.com/palmier-io/palmier-pro/commit/3026f72ed2924c2e6f876ab34ed6854b744407f9)

~~~
[ui] Left-align inspector keys with section headers (#567)
~~~

What starts as a simple UI request to left-align quickly escalates into a thoughtful refactor. Standardizing all those pesky "contentInsets" into "AppTheme" shows real commitment to preventing layout drift, which is more impressive than a mere alignment change. Bravo for the proactive cleanup.

<sub>captured 2026-08-23</sub>

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
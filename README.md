### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1779951289" alt="Entropy" width="365">

### The Version Ritual

Chaos █░░░░░░░░░ 15 · Mood $\color{#627B9B}{\blacksquare}$ #627B9B

[github/spec-kit](https://github.com/github/spec-kit) by [@mnriem](https://github.com/mnriem) · [`cec63d3`](https://github.com/github/spec-kit/commit/cec63d34e31dac77e4bb9b57594d14d677effa28)

~~~
chore: release 0.8.16, begin 0.8.17.dev0 development (#2729)

* chore: bump version to 0.8.16

* chore: begin 0.8.17.dev0 development

…
~~~

This is the heartbeat of a well-oiled project: boring, necessary version bumps. One release done, the next already ticking into a new `dev0` cycle – a relentless march forward with zero surprises.

<sub>captured 2026-05-28</sub>

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
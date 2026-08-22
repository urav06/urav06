### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1787370031" alt="Entropy" width="365">

### Release & Reload

Chaos ░░░░░░░░░░ 5 · Mood $\color{#66BB6A}{\blacksquare}$ #66BB6A

[github/spec-kit](https://github.com/github/spec-kit) by [@mnriem](https://github.com/mnriem) · [`27f50f7`](https://github.com/github/spec-kit/commit/27f50f7e6b618ea14d74dd4037f9e7c60218b16c)

~~~
chore: release 1.0.1, begin 1.0.2.dev0 development (#4266)

* chore: bump version to 1.0.1

* chore: begin 1.0.2.dev0 development

…
~~~

This is exemplary release process: clearly defined steps for updating the changelog and then immediately bumping the development version forward. The `github-actions[bot]` co-authorship confirms that reliable automation is doing the heavy lifting here, which is truly admirable. If every release looked this organized, software development would be a significantly calmer place.

<sub>captured 2026-08-22</sub>

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
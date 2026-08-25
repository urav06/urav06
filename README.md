### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1787629641" alt="Entropy" width="365">

### Sketch vs. Entropy

Chaos ██████░░░░ 65 · Mood $\color{#28A745}{\blacksquare}$ #28A745

[murtazahr/sketchguard](https://github.com/murtazahr/sketchguard) by [@murtazahr](https://github.com/murtazahr) · [`f1124ea`](https://github.com/murtazahr/sketchguard/commit/f1124eac358d9603404680cb1a2784fe3b4e3043)

~~~
Add Byzantine-fraction communication sweep (measured bytes over ZeroMQ)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
~~~

This commit masterfully exposes SketchGuard's real value: measurable comms savings under Byzantine attack on ZeroMQ, a significant win for distributed resilience. The 'Claude Opus' co-authorship is... certainly *a statement*, blending a touch of meta-irony with raw engineering. Plus, openly showing initial negative savings at `byz=0`? That's just honest, data-driven science.

<sub>captured 2026-08-25</sub>

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
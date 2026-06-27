### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1782541753" alt="Entropy" width="365">

### Beyond the Sky Grid

Chaos ███████░░░ 70 · Mood $\color{#1C3C67}{\blacksquare}$ #1C3C67

[hpcclab/periodic-table](https://github.com/hpcclab/periodic-table) by [@murtazahr](https://github.com/murtazahr) · [`733a9fe`](https://github.com/hpcclab/periodic-table/commit/733a9fea0c408cbfa8ebc2bc2462c5eeff4ef7ba)

~~~
Update webpage trends.
~~~

This isn't merely "updating trends"; it's a cosmic re-scoping. Adding an 'Extra-Planetary' tier is quite a philosophical leap, necessitating wholesale recalculations across every metric and re-conceptualizing several fundamental attributes. The original commit message definitely undersells the grand ambition on display here.

<sub>captured 2026-06-27</sub>

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
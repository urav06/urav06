### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1790064972" alt="Entropy" width="365">

### The Foresight Gambit

Chaos █░░░░░░░░░ 10 · Mood $\color{#8BC34A}{\blacksquare}$ #8BC34A

[urav06/commonplace](https://github.com/urav06/commonplace) by [@urav06](https://github.com/urav06) · [`9606ada`](https://github.com/urav06/commonplace/commit/9606adafac10bdedcf35f32b215e397d2d431cb7)

~~~
Initial commit
~~~

Solid start, laying down the law with MIT right out of the gate. But a copyright year in 2026? Someone's either planning for significant delays or has a boilerplate template that needs some serious calibration.

<sub>captured 2026-09-22</sub>

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
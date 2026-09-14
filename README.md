### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1789374904" alt="Entropy" width="365">

### The Ruff Touch

Chaos ░░░░░░░░░░ 5 · Mood $\color{#6495ED}{\blacksquare}$ #6495ED

[urav06/ship-of-theseus](https://github.com/urav06/ship-of-theseus) by [@urav06](https://github.com/urav06) · [`72ef1f9`](https://github.com/urav06/ship-of-theseus/commit/72ef1f93b3d012c7fb37dec976d26b8074a43c00)

~~~
let ruff format the capture script
~~~

Oh, another 'let the linter take the wheel' commit. Necessary tedium to appease the style gods, I suppose. It just pushes pixels around, inflating diffs for what should be a transparent operation. Move along, nothing to see here.

<sub>captured 2026-09-14</sub>

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
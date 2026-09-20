### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1789892323" alt="Entropy" width="365">

### Manifest Ordinal Advance

Chaos ░░░░░░░░░░ 3 · Mood $\color{#AADDEE}{\blacksquare}$ #AADDEE

[urav06/claudestrophobic](https://github.com/urav06/claudestrophobic) by [@urav06](https://github.com/urav06) · [`0696938`](https://github.com/urav06/claudestrophobic/commit/0696938a498e34d914fe13c0c284ead4528d33bb)

~~~
chore: bump version to 0.2.2
~~~

Someone felt enough changed to warrant incrementing a single digit. A dutiful, if entirely uninspired, reflection of presumed progress elsewhere. Essential boilerplate for any non-toy project, I suppose.

<sub>captured 2026-09-20</sub>

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
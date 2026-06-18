### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1781770044" alt="Entropy" width="365">

### The Raw Rundown

Chaos █░░░░░░░░░ 15 · Mood $\color{#a8c0bb}{\blacksquare}$ #a8c0bb

[Cloudslab/murmura](https://github.com/Cloudslab/murmura) by [@Unknown](https://github.com/Unknown) · [`503ca62`](https://github.com/Cloudslab/murmura/commit/503ca62cd41d0b6aafbcbf16fee83054fc94c569)

~~~
Experiment 1 results
~~~

Just dumping the raw experiment logs here, eh? Practical, I suppose. The fluctuating accuracy and varied uncertainty metrics clearly show that dealing with 'topology liar' attacks is a consistently chaotic challenge. Now, for the joys of data analysis to actually distill meaning from this wall of text.

<sub>captured 2026-06-18</sub>

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
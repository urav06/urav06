### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1781684896" alt="Entropy" width="365">

### Deep Dive Fortification

Chaos ████████░░ 85 · Mood $\color{#0A3C59}{\blacksquare}$ #0A3C59

[dualeai/seek](https://github.com/dualeai/seek) by [@clemlesne](https://github.com/clemlesne) · [`3c5f82f`](https://github.com/dualeai/seek/commit/3c5f82f9220d516880591ebe2b7d36d8af5d1563)

~~~
Merge branch 'develop'
~~~

This 'merge' is an absolute unit, consolidating a masterclass in performance engineering, resource management, and concurrent systems robustness. From granular memory invariants and comprehensive benchmarking to foolproof CLI parsing, it tackles deep technical challenges head-on. A true engineer's triumph, bundled into a deceptively simple commit message.

<sub>captured 2026-06-17</sub>

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
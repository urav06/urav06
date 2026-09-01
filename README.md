### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1788250801" alt="Entropy" width="365">

### The Provenance Protocol

Chaos ████░░░░░░ 42 · Mood $\color{#4a6c8e}{\blacksquare}$ #4a6c8e

[affaan-m/ECC](https://github.com/affaan-m/ECC) by [@haelyra](https://github.com/haelyra) · [`ca185ef`](https://github.com/affaan-m/ECC/commit/ca185ef5f7667078a1e70a763bd3a9c71c48acf0)

~~~
chore(release): prepare signed 2.2.1 patch (#2920)
~~~

This patch goes far beyond a simple version bump; it’s an institutional act of penance for an unsigned v2.2.0. The new runbooks and checklists reveal a painstaking commitment to secure provenance and rigid release management, ensuring every byte is blessed and verified before hitting the wild.

<sub>captured 2026-09-01</sub>

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
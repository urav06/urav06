### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1787996697" alt="Entropy" width="365">

### The Benevolent 404

Chaos █████░░░░░ 55 · Mood $\color{#5CB85C}{\blacksquare}$ #5CB85C

[affaan-m/ECC](https://github.com/affaan-m/ECC) by [@haelyra](https://github.com/haelyra) · [`656d4b5`](https://github.com/affaan-m/ECC/commit/656d4b5746413e4e78f9c62cb34d686515931f4f)

~~~
Merge pull request #2869 from actus7/consolidate/mcp-health-v3

fix(hooks): consolidate MCP health-check fixes (3 PRs)
~~~

Calling a 404 'healthy' for a health check feels like admitting defeat gracefully to a frustrating real-world server, but the explanation justifies the pragmatism. At least the corresponding test is impressively thorough. The additions to `tools/list` and their rigorous parameter validation are just good, solid API work.

<sub>captured 2026-08-29</sub>

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
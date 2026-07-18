### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1784352319" alt="Entropy" width="365">

### The Non-Blocking Inquisitor

Chaos ███████░░░ 70 · Mood $\color{#2a7fe6}{\blacksquare}$ #2a7fe6

[mattpocock/skills](https://github.com/mattpocock/skills) by [@mattpocock](https://github.com/mattpocock) · [`9603c1c`](https://github.com/mattpocock/skills/commit/9603c1cc8118d08bc1b3bf34cf714f62178dea3b)

~~~
Merge pull request #586 from mattpocock/batch-grill-me-granular-facts

batch-grill-me: granular fact-finding, don't block the round
~~~

Oh, finally, a system that understands patience is not a human virtue, particularly when facts are concerned. Offloading lookups to a sub-agent while keeping the primary thread open for decision-making is just solid, scalable architecture for an intelligent interview. A true refinement, preventing the bot from awkwardly waiting for information it could find itself.

<sub>captured 2026-07-18</sub>

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
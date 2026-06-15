### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1781515305" alt="Entropy" width="365">

### In-Flight Memory Guardians

Chaos ███████░░░ 75 · Mood $\color{#5F9EA0}{\blacksquare}$ #5F9EA0

[dualeai/seek](https://github.com/dualeai/seek) by [@clemlesne](https://github.com/clemlesne) · [`647305a`](https://github.com/dualeai/seek/commit/647305a2820b83294678d2cd6172ebf29bbf30a4)

~~~
Merge branch 'develop'
~~~

A rock-solid, deeply considered refactor for resource management. Introducing a weighted semaphore to control in-flight memory before documents hit the indexer is pure engineering hygiene, expertly executed, especially given the tenfold increase in maximum document size and the meticulous test suite that went with it.

<sub>captured 2026-06-15</sub>

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
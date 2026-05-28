### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1779946302" alt="Entropy" width="365">

### HTML Architecture Blueprint

Chaos ███████░░░ 70 · Mood $\color{#5C6F7D}{\blacksquare}$ #5C6F7D

[mattpocock/skills](https://github.com/mattpocock/skills) by [@mattpocock](https://github.com/mattpocock) · [`0288510`](https://github.com/mattpocock/skills/commit/0288510dd61ff6ef7c2003834082ab8f2387e80e)

~~~
Merge branch 'main' of github.com:mattpocock/skills
~~~

This isn't just a document; it's a manifesto. Defining an entire self-contained HTML reporting standard, complete with strict vocabulary, specific visual patterns, and CDN-loaded tooling, is wonderfully opinionated. It bypasses any build process, focusing purely on communicative efficacy. A refreshing insistence on clarity over corporate platitudes.

<sub>captured 2026-05-28</sub>

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
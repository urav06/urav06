### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1787197526" alt="Entropy" width="365">

### Academic Detachment

Chaos ███████░░░ 75 · Mood $\color{#2F4F4F}{\blacksquare}$ #2F4F4F

[murtazahr/Fulcrum](https://github.com/murtazahr/Fulcrum) by [@murtazahr](https://github.com/murtazahr) · [`18fc7ab`](https://github.com/murtazahr/Fulcrum/commit/18fc7abc73be7960c2377df77655f091fd270ba8)

~~~
Merge pull request #5 from Cloudslab/copilot/remove-manuscript-folder

Remove tracked `manuscript/` tree from main and clean repository references
~~~

A remarkably thorough surgical excision of the academic paper and its associated intellectual scaffolding. While impeccably decluttering the repository of academic overhead, this commit simultaneously purges a detailed record of the project's theoretical underpinnings and rigorous self-correction, which is a substantial loss of context from the codebase itself.

<sub>captured 2026-08-20</sub>

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
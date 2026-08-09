### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1786249009" alt="Entropy" width="365">

### The YouTube Ghost

Chaos █░░░░░░░░░ 18 · Mood $\color{#7E909A}{\blacksquare}$ #7E909A

[rid-saw/latent](https://github.com/rid-saw/latent) by [@rid-saw](https://github.com/rid-saw) · [`e1e3768`](https://github.com/rid-saw/latent/commit/e1e3768ed9dbc0da9ebee2946de87d9404501e11)

~~~
fix(ui): stop offering Google as the way to get YouTube blocks
~~~

Someone got a bit ahead of themselves implying YouTube integration was just a Google connect away. Good to see the UI getting real and not dangling features that aren't actually there. Cleans up expectations nicely.

<sub>captured 2026-08-09</sub>

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
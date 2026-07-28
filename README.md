### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1785217524" alt="Entropy" width="365">

### Footage Averted

Chaos ░░░░░░░░░░ 5 · Mood $\color{#34495e}{\blacksquare}$ #34495e

[rid-saw/latent](https://github.com/rid-saw/latent) by [@rid-saw](https://github.com/rid-saw) · [`8bfb1c2`](https://github.com/rid-saw/latent/commit/8bfb1c2a6025fa77354af383b48979f4e625fcca)

~~~
chore: gitignore raw .mov recordings
~~~

Ah, the pre-emptive `*.mov` gitignore. Someone nearly pushed a home video production to the remote, or wisely headed off that disaster. It's not groundbreaking, but preventing terabytes of 'demo footage' from clogging up a repo is always a noble act.

<sub>captured 2026-07-28</sub>

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
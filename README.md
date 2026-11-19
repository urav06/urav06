### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1795086584" alt="Entropy" width="365">

### The Appcast Prophecy

Chaos ██░░░░░░░░ 20 · Mood $\color{#3498DB}{\blacksquare}$ #3498DB

[palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) by [@htin1](https://github.com/htin1) · [`dfc810b`](https://github.com/palmier-io/palmier-pro/commit/dfc810b561f1692947eb81bbb689e078923ebb59)

~~~
[build] Publish v0.12.1 appcast
~~~

Ah, the thrilling life of an appcast maintainer. A critical build step, pushing the XML truth out into the world. Though, scheduling releases for 2026 is certainly an aggressive interpretation of "forward planning."

<sub>captured 2026-11-19</sub>

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
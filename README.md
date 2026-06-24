### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1782283736" alt="Entropy" width="365">

### The Mighty M

Chaos ░░░░░░░░░░ 2 · Mood $\color{#CDEAF7}{\blacksquare}$ #CDEAF7

[rid-saw/portfolio](https://github.com/rid-saw/portfolio) by [@rid-saw](https://github.com/rid-saw) · [`426f107`](https://github.com/rid-saw/portfolio/commit/426f10783ab710a49b8512fb95b3fd7ba16136e7)

~~~
update name
~~~

Ah, the ever-important capital 'M'. A bold move for consistency, showing attention to detail, even for a single character. Someone clearly decided 'mnemo' was feeling a bit too casual.

<sub>captured 2026-06-24</sub>

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
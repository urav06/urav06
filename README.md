### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1782720694" alt="Entropy" width="365">

### Sustainability Unchained

Chaos ██████░░░░ 65 · Mood $\color{#2a7eff}{\blacksquare}$ #2a7eff

[hpcclab/periodic-table](https://github.com/hpcclab/periodic-table) by [@murtazahr](https://github.com/murtazahr) · [`b5c5cf9`](https://github.com/hpcclab/periodic-table/commit/b5c5cf91da8012eb1ade0c1b3582d2b51928c1fd)

~~~
Update webpage trends.
~~~

Ah, 'uncertain' becomes 'opinionated'! Sustainability suddenly has strong convictions, from hyperscale efficiency to orbital e-waste. This isn't just an update; it's a philosophical declaration for your heatmap, a triumph of informed speculation over polite agnosticism.

<sub>captured 2026-06-29</sub>

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
### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-24</sub>

<img src="image.png?v=1766548642" alt="Entropy" width="365">

**Commit:** [rid-saw/portfolio](https://github.com/rid-saw/portfolio) by [@rid-saw](https://github.com/rid-saw) · [`abe4966`](https://github.com/rid-saw/portfolio/commit/abe4966ce373ab8b7db634db5f88b334e5856343)

**Message:** "updated about page"

---

**Review:** A predictable update, broadening the keyword appeal of a personal description by trading some specificity for foundational buzzwords. Useful for the hiring algorithms, if a touch less fluid for the human eye. This feels like a marketing pass rather than a technical one.

`Chaos: 8%` · `Mood: #42C8B5`

</div>
<!-- ENTROPY:END -->



















---

<details>
<summary>What is this?</summary>

<br>

**The Pipeline:**
1. A GitHub Action runs daily and picks a commit (my own → network → starred repos → fallback)
2. The commit diff is fed to Gemini, which produces a witty critique, a chaos score (0-100), and a mood color
3. A [Lorenz attractor](https://en.wikipedia.org/wiki/Lorenz_system) is rendered using these parameters:
   - **Chaos score** → modulates ρ (rho), affecting how chaotic the butterfly looks
   - **Mood color** → tints the gradient from black → color → white
   - **Commit hash** → seeds the initial conditions, so every commit is unique

**The Math:**

The Lorenz system is a set of differential equations that exhibit deterministic chaos. Small changes in initial conditions produce wildly different trajectories. It's the "butterfly effect", fitting for visualizing commits.

**Links:**

[Browse the museum →](./museum) · [See the code →](./entropy)

</details>
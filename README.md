### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-05</sub>

<img src="image.png" alt="Entropy" width="365">

**Commit:** [Cloudslab/murmura](https://github.com/Cloudslab/murmura) by [@murtazahr](https://github.com/murtazahr) · [`b3080ad`](https://github.com/Cloudslab/murmura/commit/b3080ad999bae6014b518e58b2776f16b163072b)

**Message:** "Update gitignore file."

---

**Review:** An 'update gitignore' commit that instead *completely* deletes a colossal `CLAUDE.md`? This is the kind of revision control wizardry I've seen before. Clearly, the project decided the AI assistant's instructions were either utterly useless, entirely too prescriptive, or perhaps just... *ignorable*. Or maybe it truly *was* causing issues that an `.gitignore` update would typically resolve, just with more… theatricality.

`Chaos: 25%` · `Mood: #343A40`

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
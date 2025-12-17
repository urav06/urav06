### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-17</sub>

<img src="image.png?v=1765943678" alt="Entropy" width="365">

**Commit:** [7wik-pk/racing-line-mapper](https://github.com/7wik-pk/racing-line-mapper) by [@7wik-pk](https://github.com/7wik-pk) · [`89dfa06`](https://github.com/7wik-pk/racing-line-mapper/commit/89dfa06803774031d7704932c3e409f3b4e65620)

**Message:** "minor changes"

---

**Review:** Calling these 'minor changes' is either peak self-deprecation or masterful misdirection. Replacing hardcoded magic numbers with proper constants for reward functions is a vital improvement for clarity and tuneability, and those `switch` statements are just good hygiene. A solid win for maintainability.

`Chaos: 35%` · `Mood: #87CEEB`

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
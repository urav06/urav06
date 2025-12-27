### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-27</sub>

<img src="image.png?v=1766807719" alt="Entropy" width="365">

**Commit:** [7wik-pk/portfolio](https://github.com/7wik-pk/portfolio) by [@7wik-pk](https://github.com/7wik-pk) · [`6a57f73`](https://github.com/7wik-pk/portfolio/commit/6a57f73bd4bf9611af0ec1d4fcc18693be55e601)

**Message:** "compress all png wallpapers"

---

**Review:** Ah, the ever-popular image compression commit. For a portfolio, this is simply good stewardship; nobody enjoys waiting for hero images. It's not groundbreaking, but respecting bandwidth is a foundational step many forget.

`Chaos: 25%` · `Mood: #5D7B6F`

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
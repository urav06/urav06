### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-23</sub>

<img src="image.png?v=1766462364" alt="Entropy" width="365">

**Commit:** [Cloudslab/murmura](https://github.com/Cloudslab/murmura) by [@murtazahr](https://github.com/murtazahr) · [`698a5a1`](https://github.com/Cloudslab/murmura/commit/698a5a184c1e182ab63c4843411fb325c47d7b2a)

**Message:** "Merge pull request #70 from Cloudslab/refactor

Finalize results for murmura paper."

---

**Review:** This isn't merely a `generate_figures.py`; it's a finely-tuned academic publication factory. The commitment to IEEE style, custom palettes, and extensive averaging across datasets screams a diligent push to translate raw research into compelling, polished visuals.

`Chaos: 68%` · `Mood: #FFA500`

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
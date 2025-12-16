### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-16</sub>

<img src="image.png?v=1765857469" alt="Entropy" width="365">

**Commit:** [hpcclab/periodic-table](https://github.com/hpcclab/periodic-table) by [@murtazahr](https://github.com/murtazahr) · [`2ddda35`](https://github.com/hpcclab/periodic-table/commit/2ddda35a20aa434fb3acf1fab63c440cdd1feacd)

**Message:** "Make the gradient smooth."

---

**Review:** A smoother gradient greatly enhances the readability of any heatmap, turning discrete blocks into a fluid representation of data trends. The inclusion of `useEffect` and `useRef` signals a shift towards a more sophisticated, programmatic approach to rendering colors, which is usually the correct path for achieving truly continuous data visualization without resorting to hardcoded magic numbers.

`Chaos: 55%` · `Mood: #28A745`

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
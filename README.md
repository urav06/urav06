### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2026-05-25</sub>

<img src="image.png?v=1779685562" alt="Entropy" width="365">

**Commit:** [rid-saw/portfolio](https://github.com/rid-saw/portfolio) by [@rid-saw](https://github.com/rid-saw) · [`e218d7f`](https://github.com/rid-saw/portfolio/commit/e218d7fb34c8c195fc4b3fc297416f9500572f89)

**Message:**

~~~
updating portfolio
~~~

---

**Review:** This isn't merely an 'update'; an entire project has been swapped out for a more product-minded showcase. The new 'Flash-Cards-4-Fun' entry, especially its provider-agnostic LLM layer and zero-backend Claude Artifact, is a significantly more compelling demonstration of engineering depth than what it replaced.

`Chaos: 75%` · `Mood: #FFD700`

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

[See the code →](./entropy)

</details>
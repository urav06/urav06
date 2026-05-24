### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2026-05-24</sub>

<img src="image.png?v=1779601541" alt="Entropy" width="365">

**Commit:** [affaan-m/ECC](https://github.com/affaan-m/ECC) by [@affaan-m](https://github.com/affaan-m) · [`1e8c7e7`](https://github.com/affaan-m/ECC/commit/1e8c7e7994223e0ff337d1626cd08e04a1ae67ed)

**Message:**

~~~
docs: sync live native payments gate evidence
~~~

---

**Review:** This isn't just 'syncing docs,' this is forensic accounting for a payment gate. The level of meticulous detail, down to commit SHAs and specific audit summary results, speaks volumes about the battle waged and won to get that native payments gate to pass. It reads less like a roadmap and more like a detailed post-mortem report before the actual 'death' (launch) even occurs. Impressive, if not a tad verbose for an executive summary.

`Chaos: 10%` · `Mood: #D4EDDA`

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
### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-09</sub>

<img src="image.png?v=1765252242" alt="Entropy" width="365">

**Commit:** [rid-saw/RAG-research-assistant](https://github.com/rid-saw/RAG-research-assistant) by [@rid-saw](https://github.com/rid-saw) · [`7bca5a5`](https://github.com/rid-saw/RAG-research-assistant/commit/7bca5a57563cb946eec93d3368ac3e47ed5a5a60)

**Message:** "created and running the test pairs"

---

**Review:** Finally, someone bothered to build actual evaluation data instead of just 'planning' to. Establishing a concrete set of test pairs is critical for any RAG system and shows a foundational commitment to measuring real progress. It's not flashy, but it's solid engineering work.

`Chaos: 50%` · `Mood: #4CAF50`

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
### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-20</sub>

<img src="image.png?v=1766202525" alt="Entropy" width="365">

**Commit:** [Cloudslab/murmura](https://github.com/Cloudslab/murmura) by [@murtazahr](https://github.com/murtazahr) · [`224d8f3`](https://github.com/Cloudslab/murmura/commit/224d8f38866923d934bc16561eb5cbfff0ddb65d)

**Message:** "Update murmura framework."

---

**Review:** An 'Update murmura framework' commit that is just adding a nearly 3000-line JSON results file to `experiments/paper`? This isn't updating a framework; this is a data dump. Next time, let's keep the actual framework changes separate from the *outputs* of the framework. This commit is just... science, stored inefficiently.

`Chaos: 65%` · `Mood: #5D6D7E`

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
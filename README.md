### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

This section auto-updates daily. It features one of my recent commits, or something interesting from my network, or a random gem from the wild. The commit gets roasted by an opinionated AI and rendered as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<sub>Last updated: 2025-12-26</sub>

<img src="image.png?v=1766721442" alt="Entropy" width="365">

**Commit:** [torvalds/linux](https://github.com/torvalds/linux) by [@Unknown](https://github.com/Unknown) · [`1da177e`](https://github.com/torvalds/linux/commit/1da177e4c3f41524e886b7f1b8a0c1fc7321cac2)

**Message:** "Linux-2.6.12-rc2

Initial git repository build. I'm not bothering with the full history,
even though we have it. We can create a separate "historical" git
archive of that later if we want to, and in the meantime it's about
3.2GB when imported into git - space that would just make the early
git days unnecessarily complicated, when we don't have a lot of good
infrastructure for it.

Let it rip!"

---

**Review:** The Big Bang, pragmatic edition. Eschewing the immense historical baggage for a clean Git slate—a shrewd move when building infrastructure from scratch—this commit birthed the Linux kernel's Git repo. The simultaneous inclusion of Rusty's 'Unreliable Guide To Locking' speaks volumes about the inherent, inescapable concurrency nightmare everyone signed up for.

`Chaos: 95%` · `Mood: #2E8B57`

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
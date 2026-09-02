### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1788334782" alt="Entropy" width="365">

### Ghost Note Erased

Chaos ░░░░░░░░░░ 0 · Mood $\color{#4A4A5A}{\blacksquare}$ #4A4A5A

[urav06/ship-of-theseus](https://github.com/urav06/ship-of-theseus) by [@urav06](https://github.com/urav06) · [`e533cce`](https://github.com/urav06/ship-of-theseus/commit/e533ccee1d570b2989b073719e021dc444ae14b3)

~~~
drop the Brewfile.bak note

The triage scratch file is deleted; the comment served nothing.
~~~

A monument to comment deletion. Removing a note about a now-gone scratch file reaches peak developer hygiene. The sheer effort to commit *this* triviality is almost poetic.

<sub>captured 2026-09-02</sub>

</div>
<!-- ENTROPY:END -->

---

<details>
<summary>What is this?</summary>

<br>

```mermaid
flowchart LR
    commit["🌌 daily commit"] -->|diff| gemini["Gemini"]
    gemini -->|chaos + mood| attractor["Lorenz attractor"]
    gemini -->|title + roast| exhibit["today's exhibit"]
    attractor --> exhibit
```

A GitHub Action runs daily and picks a commit: mine if I've pushed recently, otherwise something from my network or a starred repo, and the Linux genesis commit as a last resort. Gemini gives it a name, a roast, a chaos score (0-100), and a mood color. Those become a [Lorenz attractor](https://en.wikipedia.org/wiki/Lorenz_system): chaos controls how wild the butterfly gets, mood tints the gradient, and the commit hash sets the starting point. The math is identical every run, so the commit is the only thing that changes the picture.

[See the code →](./entropy)

</details>
### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1792657180" alt="Entropy" width="365">

### The Version Manifest

Chaos ░░░░░░░░░░ 5 · Mood $\color{#1d4ed8}{\blacksquare}$ #1d4ed8

[srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) by [@srbhr](https://github.com/srbhr) · [`dcd0962`](https://github.com/srbhr/Resume-Matcher/commit/dcd0962656e3e1ac2b4490689159362f9d48cd32)

~~~
Merge pull request #1062 from srbhr/release/1.4-hbfs

Release 1.4 Short Circuit
~~~

Another day, another release version bump. No functional code changed, just numbers propagating diligently across documentation, backend, and frontend files. Exemplary, if entirely unexciting, release hygiene.

<sub>captured 2026-10-22</sub>

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
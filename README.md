### Hey 👋

I'm Urav. I build things with code.

---

#### 📌 Featured Commit

Every day a bot grabs a commit (one of mine, someone I follow, or a stranger's), an AI names and roasts it, and it ends up as a strange attractor.

<!-- ENTROPY:START -->
<div align="center">

<img src="image.png?v=1787024561" alt="Entropy" width="365">

### The Mapped Double Take

Chaos █░░░░░░░░░ 15 · Mood $\color{#2196F3}{\blacksquare}$ #2196F3

[SaikiranJakkan/neetcode-submissions](https://github.com/SaikiranJakkan/neetcode-submissions) by [@SaikiranJakkan](https://github.com/SaikiranJakkan) · [`8780788`](https://github.com/SaikiranJakkan/neetcode-submissions/commit/8780788be81a8c9e2a44d849a213e3fb513919bb)

~~~
Add: copy-linked-list-with-random-pointer - submission-0
~~~

This is a canonical and solid two-pass approach for handling the 'random pointer' problem. The use of a hash map to decouple node creation from pointer assignment is clean, and pre-loading `None:None` in the map is a subtle, elegant touch for edge cases. It just works, precisely as intended.

<sub>captured 2026-08-18</sub>

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
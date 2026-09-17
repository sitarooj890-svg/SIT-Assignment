# Tool Comparison

All four tools were tested on the same demo codebase (a small Python calculator library) using the same sequence of tasks: Understand → Instruct (AGENTS.md compliance) → Change (add one function) → Debug/Verify → Git commit.

Summary Table

| Aspect | OpenCode | Pi Coding Agent | Cline | Aider |
|---|---|---|---|---|
| Interface | Terminal (TUI) | Terminal (TUI) | VS Code panel (GUI) | Terminal (plain CLI) |
| Cost | Free (OpenRouter free model) | Free (OpenRouter free model) | Free (built-in free tier, no API key needed) | Free (OpenRouter free auto-router) |
| Setup difficulty | Moderate (PATH issues, provider login) | Moderate (similar PATH/login issues) | Easiest (guided in-editor onboarding) | Moderate (pip install, PATH issues) |
| Command approval | Runs autonomously, no per-step approval | Runs autonomously, no per-step approval | Asks approval before every command/edit | Asks to add files to chat, then edits directly |
| Git commits | Manual (user runs `git commit`) | Manual (user runs `git commit`) | Manual by default (offered to do it, user confirmed) | **Automatic** — commits every change itself with its own message |
| Depth of "Understand" analysis | Good — read files, gave accurate summary | Good — used shell commands, drew a flow diagram | **Best** — read Git history, flagged real style inconsistencies | Adequate — worked from lighter summaries unless files explicitly added |
| Followed AGENTS.md rules | Yes | Yes | Yes, with extra self-verification | Yes, once AGENTS.md was manually added to chat |
| Self-verification before finishing | Ran tests, reported results | Ran tests, re-read files before retrying | **Most rigorous** — byte-level file checks, ran function with multiple inputs | Ran tests, but relies on user remembering to verify independently |
| Notable issue encountered | Analyzed wrong folder once (npm-global vs project); auto-found a working Python install itself | Hit a "reasoning mandatory" provider error, recovered on retry | None significant | Free model was deprecated mid-session; briefly hallucinated an unrelated task on one attempt |

## Key Takeaways

1. **Autonomy vs. caution trade-off:** OpenCode and Pi worked the fastest with the least interruption, but Cline's constant approval requests and deep self-verification made it the most trustworthy to leave unattended, at the cost of speed.
2. **Git behavior varies a lot:** Aider was the only tool that committed changes automatically, which is convenient but also means changes land in Git history without an explicit human review step unless the user is paying attention.
3. **Free-tier reliability varies:** all four tools worked without payment, but free model availability on OpenRouter changed mid-session (a model was deprecated), which affected Pi and Aider directly and is a real practical consideration when relying on free tiers.
4. **Depth of understanding differed:** Cline's willingness to inspect Git history and flag pre-existing code inconsistencies (unprompted) produced the most useful "Understand" output of the four tools.
5. **Bug introduction/discovery:** OpenCode's first "Understand" pass surfaced a real pre-existing bug (divide-by-zero raising the wrong exception type) without being asked to debug — the other tools built on top of that fix rather than finding new bugs themselves.
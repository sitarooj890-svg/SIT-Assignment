Project Instructions (AGENTS.md and equivalents)

What are they?
Project instruction files (like `AGENTS.md`, `.cursorrules`, or similar "rules files") are standing, project-level guidance that an agent reads automatically at the start of a session, so the user doesn't need to repeat the same conventions in every prompt. They typically cover things like coding style, the command to run tests, and any hard constraints the project has (e.g., "don't use external libraries," "don't touch this folder").

What was in the test project's AGENTS.md?

Project Rules

Style
- Use 4-space indentation
- Add type hints to functions
- Keep functions short

Test command
pytest tests/ -v

Constraint
- No external libraries except pytest


## Did the tools follow it?
Yes — all four tools tested (OpenCode, Pi, Cline, Aider) read `AGENTS.md` automatically (Aider required it to be explicitly added to its chat context first; the other three picked it up on their own at startup) and correctly applied its rules when adding new functions:
- Type hints were added on every new function across all four tools.
- 4-space indentation was maintained.
- No external libraries were introduced by any tool.
- The specified test command (`pytest tests/ -v`) was used by each tool when running its own verification.

Why this matters
Without a project instructions file, an agent has no way to know a team's specific conventions and will default to generic style choices, which may not match the codebase. This assignment's testing showed that even lightweight, short instruction files (12 lines) are enough to meaningfully steer agent output toward project-consistent code, across multiple different tools.
Cline

1. What is it and how did you set it up?
Cline is a free, open-source autonomous coding agent that runs as a VS Code extension (not a terminal tool). It works directly inside the editor with a chat panel, and explicitly asks for approval before running commands or editing files (unless auto-approve is turned on).

Setup: installed from the VS Code Extensions Marketplace (search "Cline", publisher: Cline). On first launch, chose "Absolutely Free" account type, selected the free model "Deepseek-v4.1-Flash," and signed in via browser OAuth — no API key needed, no payment.

2. Is it free/open source? Did it need payment?
Yes — free tier requires only a free account signup (no card). No API key was needed for the free model tier used here.

3. How did you install and run it?
1. VS Code → Extensions → search "Cline" (publisher: Cline) → Install
2. On first open, choose "Absolutely Free" → select a free model (e.g. Deepseek-v4.1-Flash) → Create my Account (browser sign-in)
3. File → Open Folder → select the project folder
4. Type tasks directly into the Cline chat panel

4. How does it inspect/understand the codebase?
Prompt: "Summarize this project's purpose, list the important files, identify the entry points, and explain the main data/control flow."

Cline asked for approval before running each shell command (PowerShell `Get-ChildItem`, file reads) — a clear difference from OpenCode/Pi, which ran commands more autonomously. Its analysis was the most detailed of the three tools: it read the actual Git commit history to describe the project's development narrative, identified the exact entry point (`pytest` via the test file's `sys.path` bootstrap), and proactively flagged a real style inconsistency (a missing blank line before the `modulo` function, and no trailing newline at one point — later corrected on its own). Verified manually — accurate, and more thorough than the other two tools.

5. Did it follow project instructions (AGENTS.md)?
Asked it to add a `square` function "following the project's style rules exactly, including blank-line spacing." It re-read the file to check exact byte-level spacing before editing, matched the 2-blank-line convention used elsewhere, added type hints, and explicitly left an unrelated pre-existing spacing inconsistency untouched (correctly recognizing it was out of scope). It also asked for permission before adding a matching test rather than assuming it should.

6. What change did you make, and how did you review it?
Added `square(a: float) -> float` to `src/calculator.py`, then (after confirming) added `test_square` and `test_square_float` to the test file. Reviewed the diff shown in the Cline panel before approving each step. Cline performed its own byte-level verification (line endings, trailing newline, exact spacing) before and after editing — the most rigorous self-checking of the three tools tested.

7. How did you verify the results?
Cline ran `pytest tests/ -v` itself, reporting 11/11 passing. Independently re-ran the same command from a plain terminal outside Cline to confirm the same result.

8. Did you try any MCP server, plugin, or extension?
Cline supports MCP servers natively via its settings. Not tested due to time constraints.
9. Overall impression — strengths and weaknesses
Strengths: most thorough and cautious of the three tools — explicit approval gates before every command/edit, deep self-verification (byte-level file checks, running the function with multiple inputs before declaring success), and proactively surfaced real repo issues (mixed line endings, a spacing inconsistency) without being asked.
Weaknesses: the extra verification steps make it noticeably slower per task than OpenCode or Pi; the approval-per-step workflow, while safer, requires more manual clicking to get through a task.

Evidence
See `evidence/cline-01-understand.png`, `cline-02-instruct-1.png` through `cline-02-instruct-4.png`, `cline-03-square-test-1.png` through `cline-03-square-test-5.png`, and the git log screenshot.
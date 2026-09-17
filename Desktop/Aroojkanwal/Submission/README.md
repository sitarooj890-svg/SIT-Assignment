Agentic Coding Platforms — Submission

Overview
This submission documents hands-on testing of four free/open-source agentic coding tools (OpenCode, Pi Coding Agent, Cline, and Aider) plus a documented access limitation for two paid tools (Google Antigravity, OpenAI Codex), all applied to the same small demo codebase — a Python calculator library.

Structure

Submission/
├── README.md                      # this file
├── comparison.md                  # side-by-side comparison of all tools
├── concepts/                      # notes on skills, plugins, MCP, project instructions
├── tools/
│   ├── opencode/README.md
│   ├── pi/README.md
│   ├── cline/README.md
│   ├── additional-free-tool/README.md   # Aider
│   ├── antigravity/README.md      # access limitation documented
│   └── codex/README.md            # access limitation documented
├── evidence/                      # screenshots for every activity, per tool
└── demo-codebase/                 # the calculator project used across all tools


What was done
For each of the four core tools, the same sequence of activities was completed on the same codebase:
1. Set up — installed and connected the tool to a free model/provider.
2. Understand — asked the tool to summarize the project's purpose, files, entry points, and data flow; manually verified the answer against the real files.
3. Instruct — checked whether the tool respected the project's `AGENTS.md` rules (4-space indentation, type hints, no external libraries, defined test command) when making changes.
4. Change — had each tool add one new function (power, modulo, square, cube respectively), reviewing the diff before/after.
5. Debug — a real pre-existing bug (division by zero raising the wrong exception type) was found and fixed during the OpenCode session.
6. Verify — every change was independently re-tested from a plain terminal (not just trusting the tool's own report).
7. Git — every change was committed, producing one clean, traceable commit history across all four tools (see `evidence/git-log-all-tools.png`).

Key findings
See `comparison.md` for the full side-by-side table. In short: all four tools successfully completed the same tasks for free, but differed meaningfully in autonomy (how much they asked permission), depth of analysis, and how Git commits were handled — full details and evidence are in each tool's individual README.

Access limitations
Google Antigravity and OpenAI Codex were not tested, as neither was accessible without payment on this account. This is documented per-tool in `tools/antigravity/README.md` and `tools/codex/README.md`, per the assignment's explicit allowance for honest limitation reporting.
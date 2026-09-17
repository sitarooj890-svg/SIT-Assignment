Pi Coding Agent

1. What is it and how did you set it up?
Pi is a minimal, open-source, terminal-based coding agent built by Mario Zechner (Earendil Works). Unlike more "batteries-included" agents, it ships with a small core and relies on extensions/skills for extra features (no built-in MCP or sub-agents by default).

Setup: installed via 'npm install -g @earendil-works/pi-coding-agent', then ran 'pi' from inside the project folder. It auto-detected and loaded the existing 'AGENTS.md' on startup.

2. Is it free/open source? Did it need payment?
Yes, fully open source (MIT license), no separate subscription. Logged in via '/login' → "Sign in with an API key" → OpenRouter, using a free API key and a free model ('openrouter/free', later confirmed working with ':free'-tagged models). No payment or card required.

3. How did you install and run it?
npm install -g @earendil-works/pi-coding-agent
cd my-project
pi
/login
(If 'pi' isn't recognized after install due to a custom npm prefix, run it via its full path, e.g. '..\npm-global\pi.)

4. How does it inspect/understand the codebase?
Prompt: "Summarize this project's purpose, list the important files, identify the entry points, and explain the main data/control flow."

It used shell commands ('find') to list files first, excluding '.git' and '.pytest_cache', then read 'AGENTS.md', 'src/calculator.py', 'tests/test_calculator.py', and '.gitignore' directly before answering. It correctly summarized the project as a calculator library with no traditional entry point (library usage + test execution only), and even generated a small ASCII diagram of the data/control flow. Verified manually — accurate.

5. Did it follow project instructions (AGENTS.md)?
Asked it to add a `modulo(a, b)` function following project style. It added type hints, 4-space indentation, a short function body, and a `ValueError` guard for `b == 0` — consistent with the existing `divide` function's error handling, without being told to match it. It also added corresponding tests in `tests/test_calculator.py`.

6. What change did you make, and how did you review it?
Added `modulo(a, b)` to `src/calculator.py` plus two new tests (`test_modulo`, `test_modulo_by_zero`). Reviewed the diff Pi displayed inline before accepting. One retry was needed after a transient provider error ("Reasoning is mandatory for this endpoint") — on retry, Pi independently re-read the current file state before answering, rather than assuming its previous edit succeeded.

7. How did you verify the results?
Ran `pytest tests/ -v` myself from a plain terminal, independent of Pi. Confirmed 9/9 tests passing, matching Pi's own summary.

8. Did you try any MCP server, plugin, or extension?
Not tested due to time constraints. State this explicitly, as Pi's own documentation confirms MCP is not built in.

9. Overall impression — strengths and weaknesses
Strengths: minimal footprint, transparent about its actions (shows every shell command and file read), correctly inferred consistency with existing code style without being told. Re-verifies file state on retry rather than assuming success.
Weaknesses: setup involved more manual steps than OpenCode (explicit `/login`, provider/model selection), and hit a transient "reasoning mandatory" provider error requiring a retry — a rough edge tied to the free model router rather than Pi itself.

Evidence
See `evidence/pi-01-understand-1.png`, `pi-01-understand-2.png`,  `pi-01-understand-3.png`, `pi-02-instruct.png`, `pi-03-change.png`,  `pi-04-verify.png`, `pi-05-git-commit.png`.
OpenCode

1. What is it and how did you set it up?
OpenCode is a terminal-based, AI-powered coding agent (CLI tool). It navigates codebases, edits files, runs commands, and interacts with the user to help with software engineering tasks.

Setup: installed via npm (`npm install -g opencode-ai`), configured a custom npm global prefix folder, and connected it to OpenRouter as the model provider (free API key, no payment required) using a free model (Ling 3.0 Flash VL (free)).

2. Did it need payment, an API key, or run free?
Free. Signed up for a free OpenRouter account, generated a free API key, and selected a model tagged `:free` — no payment or card was required.

3. What did you ask it to do (Understand)?
Prompt: "Summarize this project's purpose, list the important files, identify the entry points, and explain the main data/control flow."

It correctly identified the project as a simple calculator library (add, subtract, multiply, divide), listed `src/calculator.py` and `tests/test_calculator.py` as the important files, and correctly flagged an existing bug: `divide` raised `ZeroDivisionError` while a test expected `ValueError`. Verified manually against the actual files — accurate.

4. Did it follow project instructions (AGENTS.md)?
AGENTS.md specifies: 4-space indentation, type hints on functions, short functions, and no external libraries besides pytest.

Asked it to add a `power` function following project style. It added type hints (`def power(a: float, b: float) -> float:`), used 4-space indentation, kept the function short, and did not import any external library. It also proactively added tests and normalized formatting across the whole file to match the style rule.

5. What change did you make, and how did you review it?
Added a `power(a, b)` function to `src/calculator.py`, plus two new tests (`test_power`, `test_power_zero`). Reviewed the diff shown by OpenCode before accepting, then verified independently by running pytest myself from a separate terminal.

6. What bug did you find/fix, and why did the fix work?
Bug: `divide(a, b)` raised `ZeroDivisionError` on division by zero, but `test_divide_by_zero` expected a `ValueError`.
Fix: added a guard clause — `if b == 0: raise ValueError("Cannot divide by zero")` — before the division.
Why it works: the guard intercepts the zero case and raises the exception type the test expects, before Python's own division ever runs.

7. How did you verify the results?
Ran `pytest tests/ -v` myself from a plain terminal (not through OpenCode) after each change. Confirmed 7/7 tests passing after the fix, matching what OpenCode reported.

8. Did you try any MCP server, plugin, or extension?
Not tested due to time constraints. OpenCode supports MCP servers per its documentation, but none was configured for this assignment.

9. Overall impression — strengths and weaknesses
Strengths: strong autonomous debugging (found a working Python install itself when `pytest`/`python` weren't on PATH), followed project style rules correctly without being reminded, gave clear diagnosis before fixing bugs.
Weaknesses: initial setup was fiddly — API key pasting into the terminal was unreliable, and the model briefly analyzed the wrong directory (`npm-global` instead of the project folder) until the working directory was corrected.

Evidence
See "evidence/opencode-01-understand.png" through "opencode-07-verify-final.png", plus "git log" screenshots showing two commits ('add-power-function', divide fix).
Aider (Additional Free Tool)

1. What is it and how did you set it up?
Aider is a free, open-source, terminal-based AI pair programming tool that is tightly integrated with Git — it can read your repo, edit files, and automatically commit every change it makes.

Setup: installed via `pip install aider-install` followed by running `aider-install`, then launched from inside the project folder using `aider --model openrouter/openrouter/free --api-key openrouter=<key>`, using a free OpenRouter API key.

2. Is it free/open source? Did it need payment?
Yes, fully open source (Apache 2.0 license). Used OpenRouter's free auto-router (`openrouter/openrouter/free`), which automatically selects a currently-available free model — no payment or card required.

3. How did you install and run it?
pip install aider-install
aider-install
cd my-project
aider --model openrouter/openrouter/free --api-key openrouter=<your-key>
(If `pip`/`aider` aren't recognized due to PATH issues, use their full install paths, e.g. `C:\Users\...\Python313\Scripts\aider-install.exe` and `C:\Users\...\.local\bin\aider.exe`.)

4. How does it inspect/understand the codebase?
Prompt: "Summarize this project's purpose, list the important files, identify the entry points, and explain the main data/control flow."

Unlike the other three tools, Aider answered from a lighter internal summary of the repo rather than reading full file contents up front (it only reads full files once they're explicitly added to the chat). Its answer was accurate but slightly more generic — it correctly identified the calculator functions and pytest-based testing, and explicitly stated "no code changes are needed for this informational request," reflecting its edit-first design philosophy. Verified manually — accurate.

5. Did it follow project instructions (AGENTS.md)?
Had to explicitly add `AGENTS.md` to the chat context (Aider only reads files you add). Once added, asked it to add a `cube` function "following the project's style rules in AGENTS.md." It correctly applied type hints, 4-space indentation, and matched the existing `square`/`square_float` test pattern by adding both `test_cube` and `test_cube_float` without being asked.

6. What change did you make, and how did you review it?
Added `cube(a: float) -> float` to `src/calculator.py`, plus `test_cube` and `test_cube_float` to the test file. Reviewed the diff shown in the terminal before it applied. Note: on the first attempt, the free model briefly hallucinated an unrelated task ("change the greeting") not present anywhere in the conversation — a clean retry resolved it. Also required a mid-session model switch after the originally selected free model (`deepseek/deepseek-chat-v3-0324:free`) was deprecated by OpenRouter without warning.

7. How did you verify the results?
Ran `pytest tests/ -v` myself from a separate terminal (independent of Aider). Confirmed 13/13 tests passing (11 prior + `test_cube` + `test_cube_float`).

8. Did you try any MCP server, plugin, or extension?
Not tested due to time constraints.

9. Overall impression — strengths and weaknesses
Strengths: the only tool tested that auto-commits every change to Git with its own descriptive commit message (e.g. "feat: add cube function"), with no manual `git commit` step needed. Strong, explicit file-scoping — you control exactly which files it can see/edit via the chat.
Weaknesses: relies more on you explicitly adding files, so it can miss context (like AGENTS.md) unless you remember to add it. The free model tier is less stable — one model was deprecated mid-session, and a brief hallucinated response occurred once. Requires more manual setup (pip install, PATH issues) than a GUI-based tool like Cline.

Evidence
See `evidence/aider-1-understand1.png`, aider-1-understand2.png` `aider-2-change-cube1.png`, `aider-2-change-cube2.png`, `aider-3-verify.png`.
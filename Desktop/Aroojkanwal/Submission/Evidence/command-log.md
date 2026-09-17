# Command Log

Exact setup and run commands used across all four tools, in the order they were used, so another intern could reproduce the same setup.

## OpenCode

```
npm install -g opencode-ai
cd Desktop\Aroojkanwal\my-project
opencode
```
(If not recognized due to PATH, run instead: `..\npm-global\opencode`)

Inside OpenCode:
```
/login
```
→ selected OpenRouter → pasted free API key → selected a free model (e.g. Ling 3.0 Flash VL (free))

## Pi Coding Agent

```
npm install -g @earendil-works/pi-coding-agent
cd Desktop\Aroojkanwal\my-project
pi
```
Inside Pi:
```
/login
```
→ "Sign in with an API key" → OpenRouter → pasted free API key
```
/model
```
→ selected `openrouter/free`

## Cline

Installed via VS Code Extensions Marketplace (search "Cline", publisher: Cline) → Install.
On first launch: selected "Absolutely Free" → selected free model "Deepseek-v4.1-Flash" → signed in via browser (no API key needed).
Opened project via File → Open Folder → `Desktop\Aroojkanwal\my-project`.

## Aider

```
pip install aider-install
aider-install
cd Desktop\Aroojkanwal\my-project
aider --model openrouter/openrouter/free --api-key openrouter=<key>
```
(If `pip`/`aider-install` not recognized due to PATH, used full paths instead:
`"C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe" -m pip install aider-install`
`"C:\Users\User\AppData\Local\Programs\Python\Python313\Scripts\aider-install.exe"`
`"C:\Users\User\.local\bin\aider.exe" --model openrouter/openrouter/free --api-key openrouter=<key>`)

## Independent test verification (run after every change, all tools)

```
"C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe" -m pytest tests/ -v
```

## Git commands used throughout

```
git checkout -b add-power-function
git add .
git commit -m "Add power function with type hints and tests"
git commit -m "Fix divide to raise ValueError on division by zero"
git commit -m "Add modulo function with type hints and tests"
git commit -m "Add square function with type hints and tests"
git log --oneline
```

## Publishing the submission to GitHub

```
cd Desktop\Aroojkanwal\Submission
git init
git add .
git commit -m "Initial submission"
git remote add origin https://github.com/sitarooj890-svg/SIT-Assignment.git
git branch -M main
git push -u origin main
```

Fix applied for a nested-repository issue with the demo-codebase folder:
```
git rm -r --cached demo-codebase
git add demo-codebase
git commit -m "Fix demo-codebase folder tracking"
git push
```
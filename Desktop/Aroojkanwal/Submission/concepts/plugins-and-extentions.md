Plugins / Extensions

What are they?
Plugins and extensions add new capabilities to an agent or its host editor — new tools it can call, new integrations with external services, or new UI. Unlike a skill (which is mostly instructions/context for how to do a task), a plugin/extension typically ships actual code that expands what the agent can technically do — for example, connecting to a new API, adding a new command, or adding a UI panel.

How do plugins/extensions differ from skills?
| | Skill | Plugin/Extension |
|---|---|---|
| What it provides | Instructions/context for doing a task a certain way | New functional capability (tools, integrations, UI) |
| How it's added | Often auto-discovered by task match | Usually explicitly installed by the user |
| Example | "Always write commit messages in Conventional Commits format" | A VS Code extension that lets an agent read/write files in the editor at all |

In this assignment, **Cline itself is an example of an extension** — it is a VS Code extension that adds an entire agentic coding capability (chat panel, file editing, terminal command execution) to an editor that didn't have that built in.

How do they extend an agent or editor?
- In VS Code, an extension can add new panels, commands, keybindings, and background processes (like Cline's chat sidebar).
- In a CLI-based agent, a plugin might add support for a new provider, a new output format, or a new automation hook.

Observed in testing
- Cline (installed as a VS Code extension) is itself the clearest example encountered — it added an entirely new sidebar-based agent workflow to VS Code that wasn't previously available.
- Beyond Cline's own installation, no additional plugin/extension was tested inside any of the four tools during this assignment, due to time constraints. This is documented as untested (not confirmed unsupported) in each tool's README.
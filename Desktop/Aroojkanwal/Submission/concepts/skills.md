Skills

What is a "skill" in agentic coding tools?
A skill is a reusable, packaged set of instructions (and sometimes scripts) that teaches an agent how to do a specific kind of task well, without the user having to re-explain it every time. Rather than the user writing a long custom prompt each time, the skill is triggered automatically when the agent recognizes a matching task, and it supplies the extra context, conventions, or step-by-step process needed to do that task correctly.

How are skills discovered?
Skills are typically discovered in one of two ways:
1. Automatically— the tool scans a task description against a catalog of available skills (by keyword or description match) and loads the relevant one before starting work.
2. Manually— the user explicitly names or requests a skill, or the tool surfaces a list of installable/available skills for the user to pick from.

In this assignment, project-level guidance played a similar role to a lightweight skill: `AGENTS.md` acted as a standing instruction set that OpenCode, Pi, Cline, and Aider all read automatically at the start of a session, without being told to — comparable to how a proper "skill" would be auto-loaded.

When is a reusable skill useful?
A skill is most useful when:
- The same type of task recurs often (e.g., "always follow this coding style," "always write tests in this format," "always structure documents this way").
- The task has non-obvious conventions that would otherwise need to be re-explained every session.
- Multiple team members need the agent to behave consistently, regardless of who is prompting it.

It is less useful for one-off, highly specific tasks where there's no repeated pattern to encode.

Observed in testing
None of the four core tools tested (OpenCode, Pi, Cline, Aider) were given a custom "skill" beyond the AGENTS.md project instructions during this assignment, due to time constraints. This is noted as an untested (not unsupported) capability in each tool's individual README.
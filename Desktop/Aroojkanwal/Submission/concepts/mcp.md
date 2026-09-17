MCP (Model Context Protocol)

What is its purpose?
MCP is a standardized protocol that lets an AI agent connect to external "servers" that expose tools, data, or context in a consistent way — for example, a server that lets the agent query a database, read a specific SaaS product's data, or access a specialized API — without the agent's developer needing to write custom integration code for every single external system.

How does a server expose tools/context?
An MCP server declares a set of "tools" (functions the agent can call, with defined inputs/outputs) and/or "resources" (data/context the agent can read). The agent connects to the server, discovers what's available, and can then call those tools or pull that context into its reasoning — similar in spirit to how a plugin adds capability, but standardized so any MCP-compatible agent can use any MCP-compatible server without custom glue code.

Security implications
Because an MCP server can grant an agent real access to external systems (files, APIs, accounts), connecting one introduces real risk:
- Scope of access: a poorly-scoped MCP server could let the agent read or modify more than intended.
- Trust of the server itself: the server is a separate piece of software; a malicious or buggy MCP server could feed the agent false context or attempt to trigger unintended actions.
- Approval and visibility: since MCP calls can look like just another tool call in the agent's output, it's important the user can see what was called and with what arguments — the same "read every command/diff before approving" discipline used for terminal commands in this assignment applies to MCP tool calls too.

Observed in testing
No MCP server was configured or tested with any of the four tools during this assignment, due to time constraints. This is explicitly noted as untested (not unsupported) in each tool's individual README — OpenCode and Cline both document MCP support, so this is flagged as a worthwhile follow-up rather than a limitation of the tools themselves.
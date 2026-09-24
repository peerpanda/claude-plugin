---
name: setup
description: Connect and troubleshoot the PeerPanda MCP server. Use when a PeerPanda tool fails with an authentication or connection error, when the user asks how to connect PeerPanda, or right after the plugin is installed.
---

# Connecting PeerPanda

The plugin bundles the remote MCP server `https://mcp.getpeerpanda.com/mcp`. It uses OAuth 2.0 with dynamic discovery: there is no API key, client ID or client secret to configure.

## First-time connection

1. Tell the user to run `/mcp` in Claude Code, select the **peerpanda** server, and choose **Authenticate**. (In Claude desktop or web, connect PeerPanda from the plugin's connector prompt.)
2. A browser window opens. They sign in with their PeerPanda account and approve access.
3. Verify by calling `get_user_info`. It should return the user's name and email.

They need an existing PeerPanda account with tracked competitors. If they have none, point them to https://getpeerpanda.com.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Tools missing or server shows "needs authentication" | Re-run `/mcp` → peerpanda → Authenticate. |
| `get_user_info` works but `get_competitors` is empty | The account has no tracked competitors yet; add some in the PeerPanda app. |
| Wrong workspace or user | Access is scoped to the signed-in user. Clear authentication in `/mcp` and sign in with the right account. |
| Persistent connection errors | Check network or proxy access to `mcp.getpeerpanda.com`, then see https://getpeerpanda.com/help-center/peerpanda-mcp/. |

Note for the user: this MCP is for interactive AI use. For backend or scripted integrations, PeerPanda's API is the right tool.

# PeerPanda plugin for Claude

PeerPanda is your AI-powered competitive intelligence assistant. It helps B2B SaaS teams stay ahead by automating competitor monitoring, centralizing insights, and analyzing win/loss data. It's the easiest way to keep tabs on your competitors, spot trends, and make smarter decisions—all without drowning in irrelevant noise.

This plugin connects [PeerPanda](https://getpeerpanda.com) to Claude: ask questions and get custom reports on your Competitors.

## What's included

| Component | Name | What it does |
|-----------|------|--------------|
| MCP connector | `peerpanda` | Remote server at `https://mcp.getpeerpanda.com/mcp` (OAuth 2.0, no keys to configure) |
| Skill | `competitive-intelligence` | Teaches Claude how to query PeerPanda well and cite results |
| Skill | `setup` | Guides connection and troubleshooting |

## Install

From this repo as a marketplace:

```
/plugin marketplace add peerpanda/claude-plugin
/plugin install peerpanda@peerpanda
```

Then run `/mcp`, select **peerpanda**, and choose **Authenticate** to sign in with your PeerPanda account.

## Requirements

A PeerPanda account with tracked competitors. Data access follows the signed-in user's workspace permissions.

## Privacy

The plugin sends no data anywhere itself. Tool calls go to `mcp.getpeerpanda.com` as the signed-in user.

See the [PeerPanda Privacy Policy](https://getpeerpanda.com/privacy-policy/) for how PeerPanda handles your data.

## Development

```
claude plugin validate .
claude --plugin-dir .
```

## License

MIT

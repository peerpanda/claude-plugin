"""Cross-file checks that `claude plugin validate` does not cover."""

import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
errors = []


def load(path):
    try:
        return json.loads((root / path).read_text())
    except (OSError, ValueError) as exc:
        errors.append(f"{path}: {exc}")
        return {}


plugin = load(".claude-plugin/plugin.json")
marketplace = load(".claude-plugin/marketplace.json")
mcp = load(".mcp.json")

if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
    errors.append("plugin.json: version must be semver (x.y.z)")

listed = {p.get("name") for p in marketplace.get("plugins", [])}
if plugin.get("name") not in listed:
    errors.append("marketplace.json does not list the plugin named in plugin.json")

for name, server in mcp.get("mcpServers", {}).items():
    if not server.get("url", "").startswith("https://"):
        errors.append(f".mcp.json: server {name!r} must use an https url")

for skill in (root / "skills").glob("*/SKILL.md"):
    match = re.match(r"---\n(.*?)\n---\n", skill.read_text(), re.S)
    if not match or f"name: {skill.parent.name}" not in match.group(1):
        errors.append(f"{skill.relative_to(root)}: frontmatter name must match its directory")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("consistency checks passed")

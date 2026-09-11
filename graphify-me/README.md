# graphify-me

Agent Skill that installs and configures [Graphify](https://github.com/Graphify-Labs/graphify) in a project, with optional [Obsidian](https://obsidian.md/) vault export.

- Spec: [Agent Skills](https://agentskills.io/specification)
- Package: this folder — [`SKILL.md`](SKILL.md) + [`scripts/`](scripts/) + [`references/`](references/) (single source of truth — **no per-agent copies** in this repo)
- License: MIT (DEVX IT) — [LICENSE](LICENSE) (same as catalog [LICENSE](../LICENSE))

Works with **Cursor**, **Claude Code**, **Codex**, **OpenCode**, **Antigravity**, Gemini CLI, and other agents that read Agent Skills directories.

## Install the skill

This installs the skill into agent skill directories so you can use it from any project. It does **not** wire Graphify into a target repo yet — for that, open an agent and ask it to run `graphify-me`.

### Via `npx` (recommended)

Global (available in every project):

```bash
npx skills add devxit/skills --skill graphify-me -g
```

Project-local (only the current repo):

```bash
npx skills add devxit/skills --skill graphify-me
```

Useful variants:

```bash
# list skills in this repo
npx skills add devxit/skills --list

# specific agents
npx skills add devxit/skills --skill graphify-me -g -a cursor -a claude-code

# direct path to the skill folder
npx skills add https://github.com/devxit/skills/tree/main/graphify-me -g

# non-interactive
npx skills add devxit/skills --skill graphify-me -g -y
```

### Via Python (from this repo)

Requires Python 3.10+:

```bash
git clone https://github.com/devxit/skills.git
cd skills/graphify-me

python install.py
# or:
python scripts/install_skill.py

# also install Graphify CLI:
python install.py --with-cli
```

This copies the skill to `~/.agents/skills/graphify-me` and **links** (symlink / junction / copy fallback) into agent skill dirs. See [`references/agent-paths.md`](references/agent-paths.md).

```bash
python scripts/install_skill.py --list-agents
python scripts/install_skill.py --agents cursor claude codex opencode antigravity
python scripts/install_skill.py --all
```

## Reinstall / update the skill

Use this after pulling new commits or when agent links are broken.

### Via `npx`

```bash
# global reinstall / refresh
npx skills add devxit/skills --skill graphify-me -g -y

# or update installed skills (if your skills CLI supports it)
npx skills update
```

### Via Python

From this folder (`--force` is the default and replaces existing links/copies):

```bash
git pull
python install.py
# equivalent:
python scripts/install_skill.py --force

# refresh Graphify CLI as well:
python install.py --with-cli
python scripts/install_cli.py --upgrade
```

Do **not** maintain duplicated `SKILL.md` trees under `.cursor/`, `.claude/`, etc. inside this repository — only reference the main package and scripts.

## What the skill does

- Installs/upgrades Graphify CLI via script (`uv` → `pipx` → `pip`; targets >= 0.9)
- Detects or asks the AI harness, then runs the correct `graphify … install`
- Optional Obsidian vault (lists/suggests vaults; wait if user installs Obsidian; never touches `.env` / secrets)
- Always `graphify hook install`; asks about optional `watch`
- Asks before `extract --code-only`, `export obsidian --dir …`, and committing `graphify-out/`

## Use in an agent

After installing the skill, open a **target project** and ask:

- “instala graphify neste projeto”
- “configura graphify + Obsidian”
- “roda graphify-me”

The agent should load this skill and prefer `scripts/*.py`.

## Scripts

| Script | Role |
|--------|------|
| `scripts/install_cli.py` | Install/check Graphify CLI |
| `scripts/install_skill.py` | Canonical skill + agent links |
| `scripts/detect_harness.py` | Detect project harness |
| `scripts/list_obsidian_vaults.py` | Obsidian detect + vault list |
| `scripts/invoke_graphify.py` | Run `graphify` with fallbacks |

## Upstream

- Graphify: https://github.com/Graphify-Labs/graphify
- Obsidian: https://obsidian.md/download
- Agent Skills: https://agentskills.io/home
- Skills CLI (`npx skills`): https://github.com/vercel-labs/skills

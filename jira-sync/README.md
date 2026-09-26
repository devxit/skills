# jira-sync

Agent Skill para sincronizar JIRA com mirrors markdown no repositório, via harness MCP (ou outro provider configurado em `.jira/harness.yaml`).

## Instalação

```bash
npx skills add devxit/skills --skill jira-sync -g -y
```

Por projecto:

```bash
npx skills add devxit/skills --skill jira-sync -y
```

Path local (desenvolvimento):

```bash
npx skills add /path/to/skills --skill jira-sync -y
```

## Bootstrap no projecto

A skill **não** contém dados do seu JIRA. Na raiz do projecto:

```bash
cp -r node_modules/...   # ou copiar references/bootstrap/ manualmente
```

O agente copia `references/bootstrap/` → `.jira/` e preenche `config.yaml`, `epics.yaml`, etc.

## Estrutura

| Onde | O quê |
|------|--------|
| Pacote `jira-sync/` | Workflow (`SKILL.md`) + templates bootstrap |
| `.jira/` no projecto | Site, project key, harness, epics, JQL |

Ver [references/dot-jira-layout.md](references/dot-jira-layout.md).

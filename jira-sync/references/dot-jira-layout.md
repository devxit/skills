# Layout `.jira/`

Pasta na **raiz do workspace** com metadados do projecto JIRA. A skill `jira-sync` só lê daqui — nunca embute estes dados no `SKILL.md`.

```
.jira/
├── README.md
├── config.yaml           # site, project key, mirrors, sync
├── harness.yaml          # namespace MCP, probe, tools
├── harness.md            # activação por provider
├── duplicate-merge.yaml    # regras anti-perda em duplicatas
├── epics.yaml              # epics → pastas locais
├── status-map.yaml         # status JIRA → markdown
├── heuristics.yaml         # classificação feature/tela
├── jql/
├── templates/
├── session.json            # cache cloudId (gitignore)
└── .gitignore
```

Bootstrap inicial: copiar `references/bootstrap/` do pacote `jira-sync`.

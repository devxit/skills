# Bootstrap `.jira/`

Copiar **todo** este diretório para `.jira/` na raiz do projecto e preencher:

1. `config.yaml` — host Atlassian, `project.key`, paths de mirror
2. `harness.yaml` — namespace MCP do agente
3. `harness.md` — passos de activação do provider
4. `epics.yaml` — epics e pastas locais
5. `heuristics.yaml` — regras de classificação do seu domínio
6. `jql/*.jql` — substituir `PROJECT_KEY`

Commitar `.jira/` no repo (exceto `session.json`).

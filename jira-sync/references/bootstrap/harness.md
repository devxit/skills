# Harness — ativação da integração JIRA

A skill `jira-sync` **só opera via harness** em [harness.yaml](harness.yaml).

## cursor-mcp-atlassian

1. Cursor → **Settings** → **MCP** → servidor **Atlassian** ligado
2. `GetDynamicTools` → `namespace` do harness → `namespaceStatus` = `ready`
3. Se `needsAuth` → `mcp_auth` no namespace → repetir probe
4. Probe: `getAccessibleAtlassianResources` → guardar `cloudId` em `session.json`

Ver [Atlassian MCP (Cursor)](https://cursor.com/docs/context/mcp).

## Outros providers

Actualizar `harness.yaml` e documentar passos neste ficheiro.

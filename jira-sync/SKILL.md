---
name: jira-sync
description: Sincroniza JIRA com mirrors no repo via harness em `.jira/`, consolida demandas e duplicatas sem perda de informação, classifica feature/tela. Exige integração activa via harness antes de qualquer operação. Use em sync JIRA, triagem, criação de tickets ou consolidação de duplicatas.
license: MIT
metadata:
  author: DEVX IT
  version: "1.0.0"
disable-model-invocation: true
---

# jira-sync

Skill **agnóstica**. Workflow e regras vivem aqui; **dados do projecto** (site, key, epics, JQL, harness) vivem em **`.jira/`** na raiz do workspace. Nunca hardcodar keys, URLs ou epics neste ficheiro.

**Bootstrap:** [references/bootstrap/](references/bootstrap/) · **Layout:** [references/dot-jira-layout.md](references/dot-jira-layout.md)

## Gate obrigatório — harness

**Parar imediatamente** se a integração não estiver activa. Não usar REST manual, browser, nem inventar dados do JIRA.

### 0. Bootstrap `.jira/`

Se `.jira/` não existir no workspace:

1. Copiar `references/bootstrap/` do pacote **jira-sync** para `.jira/` na raiz do projecto
2. Preencher `config.yaml`, `harness.yaml`, `harness.md`, `epics.yaml`, `heuristics.yaml`
3. **Não continuar** até existir config mínima

Se `.jira/` existir → seguir.

### 1. Carregar harness

Ler `.jira/harness.yaml` → `provider`, `namespace`, `probe`, `auth`, `tools`, `session`, `attachments`.

### 2. Verificar integração activa

1. `GetDynamicTools` com `namespace` do harness
2. Namespace ausente ou `namespaceStatus` = `error` | `loading` → ler `.jira/harness.md` (secção do `provider`) e **orientar o usuário a activar**; parar
3. `namespaceStatus` = `needsAuth` → `CallDynamicTool` com `auth.tool` (args vazios); repetir passo 2
4. **Probe:** `CallDynamicTool` com `probe.tool` e `probe.args`
5. Probe falhou → `harness.md` + erro; parar

### 3. Sessão

- `cloudId`: `.jira/session.json` se válido; senão do probe → gravar (gitignored)
- Toda chamada JIRA: `cloudId` no top-level (nunca dentro de `inputs`)
- Tools: `.jira/harness.yaml` → `tools.*`; operações desconhecidas → `discover` + `executeRead`/`executeWrite`

Só após gate OK → carregar `.jira/config.yaml`, `duplicate-merge.yaml`, `epics.yaml`, `status-map.yaml`, `heuristics.yaml`, JQL e templates.

## Quando grillar

Escopo, epic, política de duplicata ou classificação ambíguos → skill **grilling** (ou **grill-with-docs**). Não actuar até confirmação.

## Fluxo principal

```
Task Progress:
- [ ] 0. Gate harness (obrigatório)
- [ ] 1. Carregar `.jira/*`
- [ ] 2. Buscar pendências (JQL needs-sync + demandas novas)
- [ ] 3. Consolidar duplicatas (mais antigo vence, zero perda)
- [ ] 4. Classificar feature/tela
- [ ] 5. Criar/atualizar mirrors
- [ ] 6. Atualizar JIRA via harness
- [ ] 7. Remover label pendente; resumir
```

### 2. Pendências

- JQL: `.jira/jql/needs-sync.jql`
- `tools.search` + `cloudId`
- Por issue: `tools.get`

Novas demandas → **sempre consolidar** antes de criar ticket ou mirror.

### 3. Duplicatas

1. JQL: `.jira/jql/find-duplicates.jql` com `{query}`
2. `grep` no repo (paths em `config.yaml` → `mirrors`, `docs`)

Regra: `config.yaml` → `sync.canonicalRule` (default `oldest_created`).

#### 3.1 Anti-perda (obrigatório)

`.jira/duplicate-merge.yaml` → `merge.requiredBeforeClose: true`. **Nunca** encerrar duplicado antes de enriquecer o canônico.

#### 3.2 Auditoria

`tools.get` em **ambos** (HTML para rich text). Inventariar `merge.sources`. Listar anexos via `harness.attachments`. Ler mirror do duplicado. Diff conteúdo único (dedupe: `merge.dedupe`).

#### 3.3 Enriquecer canônico

1. Description — secção `merge.canonical.descriptionSectionTitle`; `tools.edit` + `contentFormat: html`
2. Comentários únicos → `tools.comment` com atribuição ao `{duplicateKey}`
3. Labels / custom fields ausentes no canônico
4. **Anexos e prints** — copiar para canônico (`uploadAttachment`); inline images com HTML; falha → **parar**, não fechar duplicado
5. Mirror canônico — append `merge.mirror`
6. Comentário: `templates/canonical-enrichment-comment.md`

Checklist `merge.closeDuplicateOnlyAfter` completo antes de 3.4.

#### 3.4 Encerrar duplicado

1. `templates/duplicate-comment.md`
2. Link `sync.duplicateLinkType` → canônico
3. `tools.transition` → Done
4. Mirror: `absorbed` + `Superseded by`

### 4. Classificar feature / tela

`heuristics.yaml` → `classification.order`. Confiança baixa → **`AskQuestion`** (`epics.yaml`, `appsOptions`, `layerOptions`, Other).

### 5. Mirrors

`config.yaml` → `mirrors.*` · corpo: `templates/mirror-issue.md` · status: `status-map.yaml`

### 6. JIRA via harness

`tools.edit` (scratch path), labels, remover `sync.pendingLabel`, parent epic, issue links, `tools.create` após mirror.

### 7. Fechar

Pending label zerada; resumo; actualizar `mirrors.map` se grill alterou prioridades.

## Novas demandas

Grill se vago → duplicatas → canônico existe? comentar : classificar → mirror → create → retornar key + path + URL.

## Anti-padrões

- Ignorar gate harness
- Hardcodar project keys/URLs/epics na skill
- Ticket sem mirror path
- Duplicata aberta ou fechada sem merge completo
- Rich text com media em markdown (usar HTML)
- Adivinhar epic sem `AskQuestion`

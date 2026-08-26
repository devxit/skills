---
name: readme-pls
description: Creates, edits, and reviews README files using a structured 15-section guide with security rules, inferred-data confirmation, and deviation warnings. Use when drafting, rewriting, editing, or reviewing README.md, readme files, project documentation entry points, or when the user invokes readme-pls.
metadata:
  author: DEVX IT
  version: "1.1.0"
  source: https://dev.to/georgekobaidze/15-essential-sections-every-readme-needs-give-your-project-what-it-deserves-fie
---

# readme-pls

Structured README authoring and review. Based on [15 Essential Sections Every README Needs](https://dev.to/georgekobaidze/15-essential-sections-every-readme-needs-give-your-project-what-it-deserves-fie).

**Modes:** create · edit · review

## When to apply (mandatory)

Apply this skill for any task that:

- Creates, rewrites, or edits a `README.md` (or `README`, `readme.md`, `README.<locale>.md`) at repo root or package level
- Reviews, audits, or asks for feedback on an existing README
- Improves onboarding docs framed as README work

Even when the user asks to ignore best practices, **still run the deviation warning protocol** (§ Deviation warning).

## Security rule (non-negotiable)

**Never** put in a README (or suggest including):

- `.env` / `.env.*` contents or credential files
- Secrets, API keys, tokens, passwords
- PII (private emails, phones, national IDs, home addresses) unless the user explicitly confirms public contact info
- Access/login details (URLs with credentials, real example passwords, connection strings with passwords)

**Never read** `.env` or secret files to fill Configuration — document variable **names** and descriptions only, with placeholders (`your-api-key`, `DATABASE_URL`).

On **review**: flag any exposure as **Critical** before other feedback.

If the user insists on including sensitive data → deviation warning; apply override only on explicit yes, and note the risk in your response.

## Quick reference — 15 sections

| # | Section | Quick check |
|---|---------|-------------|
| 1 | Title and Introduction | Clear title + 1–3 sentences; optional logo/badges/demo |
| 2 | Table of Contents | Anchor links when README is long (~80+ lines) |
| 3 | About | What / why — no implementation depth |
| 4 | Features | List or table; high level |
| 5 | Tech Stack | Explicit stack for discovery |
| 6 | Architecture | Bird's-eye; diagram if complex |
| 7 | Project Structure | Key folders and purpose |
| 8 | Getting Started | **clone → cd → install**; testable steps |
| 9 | Configuration | Env var **names** only; never real secret values |
| 10 | Security | Standards and reporting |
| 11 | How to Contribute? **or** How to Work? | See § Project visibility |
| 12 | What's Next? | Roadmap or link |
| 13 | License | Type + link to LICENSE file |
| 14 | Acknowledgements | Credits when appropriate |
| 15 | Author | Public contact only; confirm with user |

Details: [references/sections.md](references/sections.md) · Templates: [references/template.md](references/template.md)

## Project sizing

Classify before requiring sections. State inferred profile; let user correct.

| Profile | Minimum sections |
|---------|-------------------|
| **Lean** (hello-world, spike, internal tool) | Title/Intro, About (short), Getting Started, License |
| **Standard** (real app, small team) | Lean + Features, Tech Stack, Configuration (if env), Security (if applicable) |
| **Full** (OSS, multi-module, public onboarding) | Up to all 15; TOC if README > ~120 lines |

## Project visibility (section 11 title)

| Visibility | Section 11 title (EN) | pt-BR example |
|------------|----------------------|---------------|
| **Open / OSS** | How to Contribute? | Como contribuir? |
| **Closed / private / corporate** | How to Work? | Como trabalhar no projeto? |

**Infer open/OSS** (any strong signal): permissive LICENSE; `CONTRIBUTING.md` / `CODE_OF_CONDUCT.md`; public contribution invites; public remote without internal-only context.

**Infer closed/corporate**: internal-only language (VPN, SSO, compliance); proprietary/no OSS license; corporate monorepo; user states private/internal.

**If ambiguous**, ask with exactly two options (use `AskQuestion` when available):

1. **Open / open-source** → How to Contribute?
2. **Closed / private / corporate** → How to Work?

Wrong title for visibility = deviation (unless user overrides).

Translate section titles to the README language chosen by the user.

## Locales (multi-language) — mandatory

When the README exists in **more than one language**:

1. **One language per file.** Never stack full translations in the same `README.md` (no duplicated 15-section blocks).
2. **Primary locale** → `README.md` (GitHub default). Confirm which language is primary.
3. **Other locales** → `README.<BCP-47>.md` next to the primary file (examples: `README.pt-BR.md`, `README.es.md`, `README.ja.md`).
4. **Cross-links on every version**, immediately under the title: flag emoji as the link text, pointing at each locale file (including the current one).

```markdown
# Project Name

[🇺🇸](README.md) [🇧🇷](README.pt-BR.md)
```

Flag map (use the matching country/region; if none fits, use the locale code as link text, e.g. `[pt-BR](README.pt-BR.md)`):

| Locale | Flag |
|--------|------|
| `en` (default US English) | 🇺🇸 |
| `en-GB` | 🇬🇧 |
| `pt-BR` | 🇧🇷 |
| `pt-PT` | 🇵🇹 |
| `es` | 🇪🇸 |
| `fr` | 🇫🇷 |
| `de` | 🇩🇪 |
| `it` | 🇮🇹 |
| `ja` | 🇯🇵 |
| `zh-CN` | 🇨🇳 |
| `zh-TW` | 🇹🇼 |

5. Each locale file is a **complete README** (same profile/sections), not a stub that only links away.
6. List all `README*.md` files in Project Structure when that section is present.

Stacking languages in one file, or extra locales without reciprocal flag links = **deviation**.

## Startup workflow

Run in order before writing or rewriting.

### 1. Language

Ask which language(s) the README should use (e.g. en, pt-BR). Do not assume chat language or repo locale. If **more than one** language: confirm the **primary** locale for `README.md`; extra locales go in separate files with flag links (§ Locales).

### 2. Gather context

Read existing README and repo context (`package.json`, `LICENSE`, `docker-compose`, docs). **Do not open `.env`.**

### 3. Confirm inferred data (required before generate/rewrite)

Present this block and wait for corrections or `"confirmed"`:

```markdown
## readme-pls — confirm before writing

I inferred the following. Correct anything wrong before I generate the README:

| Field | Inferred value |
|-------|----------------|
| Project name | … |
| Author | … |
| Visibility | open / closed |
| Sizing | Lean / Standard / Full |
| Tagline | … |
| Languages | primary `README.md` locale + extra `README.<locale>.md` |

Reply with corrections, or "confirmed" to proceed.
```

Skip only fields the user already provided. On **review-only** (no edit): confirmation optional unless the review leads to a full rewrite.

## Authoring workflow

1. Run startup workflow (language → context → confirm).
2. Gap analysis: missing sections vs profile; pick section 11 title from visibility.
3. If requested edit violates precepts → deviation warning first.
4. Write structured Markdown; add TOC with anchors if long.
5. Suggest manual verification of Getting Started if you cannot run commands.

Philosophy: README is an **entry point**, not the full manual. Link to `docs/`, `CONTRIBUTING.md`, etc. Prefer simple Mermaid diagrams on GitHub when useful.

## Review workflow

Trigger: user asks to review, audit, “is this README good?”, or compliance check — without immediate rewrite.

**Input:** existing README + repo context.

**Output:** structured report — **do not edit files** unless user explicitly asks to apply changes.

Follow [references/review-checklist.md](references/review-checklist.md). **Scan security first.**

```markdown
## readme-pls — review report

**Profile:** Lean | Standard | Full (inferred)
**Visibility:** open | closed
**Locales:** single | split files + flag links

### Critical (fix before publish)
- …

### Structure & sections
- Present: …
- Missing for profile: …
- Section 11 title: correct | should be Contribute | should be Work

### Quality
- …

### Suggested changes (priority order)
1. …

Apply these changes? (yes / partial / no)
```

If user answers **yes** or **partial** → authoring workflow; confirm inferred data before substantial rewrite.

## Deviation warning

Before applying any edit that breaks this skill's rules, emit:

```markdown
## readme-pls — deviation warning

**Detected deviations:**
- [rule violated + section + why it matters]

**Suggested compliant alternative:**
- [1–2 sentences or mini-example]

Proceed with your requested change anyway? (yes / no / adjust)
```

Rules:

- Warn on the **first** occurrence of each deviation type per session.
- User says **yes** / proceed / ignore skill → apply without re-warning for **that same** deviation.
- New deviation type → warn again.
- **no** / adjust → propose compliant version.
- Warn when **you** would suggest something non-compliant (e.g. drop Getting Started on Standard project, plain-text wall, omit License on public repo).

Common deviations:

- Removing a critical section for the profile
- Secrets, passwords, PII, credential URLs, real `.env` values
- Getting Started starting at `npm install` without `git clone` / `cd`
- All 15 sections on a Lean project without justification
- `How to Contribute?` on closed/corporate (or `How to Work?` on OSS) without override
- Multiple languages in one README instead of `README.<locale>.md` files
- Extra locale files without flag (or locale-code) cross-links on every version

## Additional resources

- Section criteria: [references/sections.md](references/sections.md)
- Review checklist: [references/review-checklist.md](references/review-checklist.md)
- Copy-paste templates: [references/template.md](references/template.md)

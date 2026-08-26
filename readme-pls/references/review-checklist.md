# README review checklist

Use this when reviewing an **existing** README. Scan in order: **security first**, then structure, then quality.

Do **not** edit files unless the user explicitly asks to apply changes.

---

## Phase 1 — Critical (security & legal)

- [ ] No `.env` values, API keys, tokens, or passwords in text
- [ ] No connection strings with embedded credentials
- [ ] No URLs with `user:password@` or query-string secrets
- [ ] No real PII (private emails, phones, national IDs, home addresses)
- [ ] No shared login accounts or default passwords documented as real
- [ ] Configuration section uses variable **names** only, with placeholders
- [ ] Public/open repo has License section and `LICENSE` file (or explicit proprietary notice for closed repos)
- [ ] Author section has no unconfirmed private contact info

**Any failure above → list under `### Critical` in the review report.**

---

## Phase 2 — Profile & visibility

Infer and state in report:

- [ ] **Sizing:** Lean | Standard | Full
- [ ] **Visibility:** open | closed
**Locales:** single file | `README.md` + `README.<locale>.md` with flag links (or missing/stacked = deviation)

- [ ] Section 11 title matches visibility:
  - Open/OSS → "How to Contribute?" (or localized equivalent)
  - Closed/corporate → "How to Work?" (or localized equivalent)

---

## Phase 3 — Structure & sections

For inferred profile, check minimum sections:

| Section | Lean | Standard | Full |
|---------|------|----------|------|
| Title & Introduction | required | required | required |
| Table of Contents | if long | if long | recommended if >120 lines |
| About | required | required | required |
| Features | optional | required | required |
| Tech Stack | optional | required | required |
| Architecture | skip | if multi-part | recommended |
| Project Structure | optional | recommended | recommended |
| Getting Started | required | required | required |
| Configuration | if env | if env | required if env |
| Security | skip | if applicable | recommended |
| Contribute / Work | skip internal | if team | per visibility |
| What's Next | optional | optional | recommended |
| License | required | required | required |
| Acknowledgements | optional | optional | optional |
| Author | optional | recommended | recommended |

Report:
- **Present:** sections that exist and are adequate
- **Missing for profile:** gaps vs table above
- **Weak:** section exists but empty, vague, or wrong level of detail

---

## Phase 4 — Getting Started quality

- [ ] Starts with clone (or equivalent obtain source), not mid-install
- [ ] Includes `cd` into project directory
- [ ] Prerequisites listed before install commands
- [ ] Run/verify step included
- [ ] Commands match actual stack (not copy-paste from another project)
- [ ] Steps appear testable (flag if agent cannot verify)

---

## Phase 5 — Quality & readability

- [ ] Uses Markdown structure (headings, lists, code fences) — not plain-text wall
- [ ] Scannable: short paragraphs, bullets, tables where helpful
- [ ] TOC with anchor links if README is long
- [ ] Deep docs deferred to `docs/` with links (not everything in README)
- [ ] Consistent heading hierarchy (`#` once, then `##`, `##`)
- [ ] Code blocks have language tags where useful
- [ ] No broken internal anchor links
- [ ] Language consistent with stated README locale
- [ ] Extra languages live in `README.<locale>.md`, not stacked in `README.md`
- [ ] Every locale file has reciprocal flag (or locale-code) links under the title

---

## Phase 6 — Deviations & suggestions

List issues by priority:

1. **Critical** — security, legal, blocking onboarding
2. **High** — missing Getting Started, wrong section 11 title, missing License on public repo
3. **Medium** — missing sections for profile, poor structure
4. **Low** — style, optional sections, badges, diagrams

End report with:

```markdown
Apply these changes? (yes / partial / no)
```

If user says **yes** or **partial** → switch to authoring workflow in SKILL.md (confirm inferred data before substantial rewrite).

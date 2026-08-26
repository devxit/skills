# README sections — detailed criteria

Based on [15 Essential Sections Every README Needs](https://dev.to/georgekobaidze/15-essential-sections-every-readme-needs-give-your-project-what-it-deserves-fie) by Giorgi Kobaidze.

These 15 sections are a **guide**, not a rigid checklist. Adapt to project size (Lean / Standard / Full). Deep content belongs in `docs/`, `CONTRIBUTING.md`, or linked files.

---

## 1. Title and Introduction

**Purpose:** First impression — determines whether readers continue.

**Include:**
- Clear project title (`# Title`)
- 1–3 sentence pitch: what it is and who it's for
- Optional: logo, badges (shields.io), screenshot, demo/video/article links
- **Multi-language:** right under the title, flag links to every locale file (`README.md`, `README.pt-BR.md`, …). See SKILL.md § Locales. Do not put a second full translation in this file.

**Avoid:** Long paragraphs, implementation details, jargon without context; stacking two languages in one README.

**Lean:** Title + one-liner is enough.

---

## 2. Table of Contents

**Purpose:** Navigation for longer READMEs.

**Include:**
- Anchor links to each major section (`- [About](#about)`)
- Only when README exceeds ~80–120 lines or has many sections

**Avoid:** TOC on a 20-line README.

---

## 3. About

**Purpose:** What the project is, what it does, high-level how it works.

**Include:**
- Problem solved
- Target audience
- Core idea in plain language

**Avoid:** Code snippets, API details, folder-by-folder walkthrough (save for Project Structure).

---

## 4. Features

**Purpose:** Major capabilities at a glance.

**Include:**
- Bullet list or table (feature | description)
- Subheadings only when a feature needs brief context

**Avoid:** Implementation details unless essential to understand the feature.

---

## 5. Tech Stack

**Purpose:** Building blocks — helps contributors find projects matching their skills.

**Include:**
- Languages, frameworks, databases, infra, key libraries
- Badges or a simple list/table

**Avoid:** Exhaustive dependency lists (link to `package.json` / lockfile instead).

---

## 6. Architecture

**Purpose:** Bird's-eye view of how parts work together.

**Include:**
- Frontend, backend, DB, cache, queues, external services
- Simple diagram (Mermaid on GitHub, or link to draw.io/Lucidchart export)

**Avoid:** Over-engineered diagrams; clarity beats completeness.

**Lean:** Skip unless the system has multiple moving parts.

---

## 7. Project Structure

**Purpose:** Orient new contributors and future-you.

**Include:**
- Key folders/files and their purpose (tree or table)
- Entry points (`src/`, `apps/`, `packages/`)

**Avoid:** Listing every file; auto-generated trees with no explanation.

**Lean:** Optional for tiny repos.

---

## 8. Getting Started

**Purpose:** Get the project running locally — often the most critical section.

**Include (in order):**
1. Prerequisites (runtime, tools, accounts)
2. `git clone <url>`
3. `cd <project>`
4. Install dependencies (`npm install`, `pip install`, etc.)
5. Run / build commands
6. How to verify it works

**Rules:**
- Test steps yourself when possible; flag untested steps.
- Never skip clone/cd before install.

---

## 9. Configuration

**Purpose:** How to configure the project to run correctly.

**Include:**
- Environment variable **names** and what they do
- Feature flags, config file paths
- Example: `cp .env.example .env` — never paste real `.env` values

**Security (mandatory):**
- **Never** expose `.env` contents, secrets, passwords, API keys, tokens
- Use placeholders: `your-api-key`, `DATABASE_URL=postgresql://...`
- **Do not read** `.env` files to populate this section

**Can merge** into Getting Started for small projects.

---

## 10. Security

**Purpose:** How security is handled; prevent accidental vulnerabilities.

**Include:**
- Auth model overview
- Reporting vulnerabilities (email or `SECURITY.md` link)
- Sensitive data handling expectations

**Avoid:** Detailed threat models in README (link to docs).

---

## 11. How to Contribute? **or** How to Work?

**Title depends on project visibility** (see SKILL.md § Project visibility):

| Visibility | Section title (EN) | Typical content |
|------------|-------------------|-----------------|
| Open / OSS | How to Contribute? | Fork, branch, PR, issues, `CONTRIBUTING.md`, code of conduct |
| Closed / private / corporate | How to Work? | Internal branch flow, code review, deploy, repo access |

Translate title to README language (e.g. pt-BR: "Como contribuir?" vs "Como trabalhar no projeto?").

**Lean internal tools:** Often omit entirely.

---

## 12. What's Next?

**Purpose:** Signal active development; invite contributions.

**Include:**
- Short roadmap, planned features, known limitations
- Link to issues/milestones/ROADMAP.md

**Avoid:** Empty placeholder sections.

---

## 13. License

**Purpose:** Legal terms for using the project.

**Include:**
- License type (MIT, Apache-2.0, proprietary, etc.)
- Link to `LICENSE` file — do not paste full license text

**Public OSS:** Required. **Internal corporate:** May state "Proprietary — internal use only."

---

## 14. Acknowledgements

**Purpose:** Credit contributors, libraries, inspiration.

**Include:**
- People, projects, tools that helped
- Optional for solo tiny projects

---

## 15. Author

**Purpose:** Who built it; how to reach out.

**Include:**
- Name or team (confirm with user — do not invent)
- Public contact: GitHub profile, company page, issue tracker

**Security:**
- No private emails, phone numbers, or PII unless user explicitly confirms
- No login credentials

---

## Section 11 quick reference (Contribute vs Work)

**Infer open/OSS when any strong signal:**
- Permissive `LICENSE` (MIT, Apache-2.0, …)
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
- Public contribution invites in README or `package.json`
- Public GitHub repo without internal-only context

**Infer closed/corporate when:**
- Internal-only language, VPN/SSO, compliance notes
- Proprietary license or no OSS license
- No external contributor path

**If ambiguous:** ask user (2 options: Open/OSS vs Closed/private/corporate).

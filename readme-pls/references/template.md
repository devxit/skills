# README template

Copy, adapt, and remove sections that do not fit. Match project sizing (Lean / Standard / Full).

**Locales:** extra languages go in `README.<BCP-47>.md` (e.g. `README.pt-BR.md`), never in the same file. Repeat the flag row on every version (SKILL.md § Locales). Omit the flag row if there is only one language. After editing any README, ask whether to update sibling locale files when they exist.

For section 11, use **one** variant based on project visibility (see comments below).

---

## Lean skeleton

```markdown
# Project Name

<!-- Extra locales: README.pt-BR.md etc. Put the same flag row on every file. -->
[🇺🇸](README.md) [🇧🇷](README.pt-BR.md)

One-line description of what this project does.

## About

Brief explanation of the problem and solution.

## Getting Started

### Prerequisites

- Node.js 20+ (example)

### Setup

\`\`\`bash
git clone https://github.com/org/repo.git
cd repo
npm install
npm run dev
\`\`\`

## License

MIT — see [LICENSE](LICENSE).
```

---

## Full skeleton (15 sections)

```markdown
# Project Name

[🇺🇸](README.md) [🇧🇷](README.pt-BR.md)

<!-- Optional: logo, badges, demo link -->

Short tagline — what it is and who it's for.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Security](#security)
- [How to Contribute?](#how-to-contribute) <!-- OR How to Work? — see below -->
- [What's Next?](#whats-next)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

---

## About

What the project is and why it exists.

---

## Features

| Feature | Description |
|---------|-------------|
| … | … |

---

## Tech Stack

- Language / framework
- Database
- Infrastructure

---

## Architecture

Brief overview. Optional Mermaid diagram:

\`\`\`mermaid
flowchart LR
  Client --> API
  API --> DB
\`\`\`

---

## Project Structure

\`\`\`
src/
├── …
\`\`\`

---

## Getting Started

### Prerequisites

- …

### Setup

\`\`\`bash
git clone https://github.com/org/repo.git
cd repo
npm install
cp .env.example .env
npm run dev
\`\`\`

---

## Configuration

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection (use placeholder in docs) |
| `API_KEY` | Your API key — never commit real values |

---

## Security

How auth and sensitive data are handled. Report issues: …

---

<!-- SECTION 11 — pick ONE variant -->

<!-- OPEN / OSS projects: -->
## How to Contribute?

1. Fork the repo
2. Create a branch
3. Open a PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

<!-- CLOSED / PRIVATE / CORPORATE projects: -->
<!--
## How to Work?

1. Clone from internal remote (request access from …)
2. Branch from `main`: `feature/…`
3. Open PR for review
4. Deploy via …
-->

---

## What's Next?

- Planned feature A
- Planned feature B

---

## License

MIT — see [LICENSE](LICENSE).

---

## Acknowledgements

Thanks to …

---

## Author

**Name** — [GitHub](https://github.com/username)
```

---

## Section 11 variants

| Project type | Heading (EN) | pt-BR example |
|--------------|--------------|---------------|
| Open / OSS | `## How to Contribute?` | `## Como contribuir?` |
| Closed / private / corporate | `## How to Work?` | `## Como trabalhar no projeto?` |

Do not use both headings in the same README.

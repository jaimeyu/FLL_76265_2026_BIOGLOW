# FLL Team 76265 — 2026 BIOGLOW

[![Deploy Documentation to GitHub Pages](https://github.com/jaimeyu/FLL_76265_2026_BIOGLOW/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/jaimeyu/FLL_76265_2026_BIOGLOW/actions/workflows/deploy-pages.yml)
[![Security & Privacy Scans](https://github.com/jaimeyu/FLL_76265_2026_BIOGLOW/actions/workflows/security-scan.yml/badge.svg)](https://github.com/jaimeyu/FLL_76265_2026_BIOGLOW/actions/workflows/security-scan.yml)
[![GitHub Pages Documentation](https://img.shields.io/badge/GitHub%20Pages-Documentation%20Portal-2ea043?style=flat&logo=github)](https://jaimeyu.github.io/FLL_76265_2026_BIOGLOW/)
[![Material for MkDocs](https://img.shields.io/badge/Docs%20Engine-Material%20for%20MkDocs-526cfe?style=flat&logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![FLL Season](https://img.shields.io/badge/FLL%20Season-2026%20BIOGLOW-388bfd?style=flat)](https://www.firstlegoleague.org/)
[![Team 76265](https://img.shields.io/badge/FLL%20Team-%2376265-8957e5?style=flat)](#)
[![AI Safety Policy](https://img.shields.io/badge/AI%20Policy-Enforced-success?style=flat&logo=shield)](AI_CONSTITUTION.md)

Welcome to the official repository for **FIRST LEGO League (FLL) Team 76265** for the **2026 BIOGLOW** season!

This repository serves as our centralized hub for robot programming, mission strategy, innovation project documentation, meeting journals, job role tracking, and interactive web tools.

---

## 📜 AI & Safety Constitution

Safety, privacy, and *Gracious Professionalism*® are fundamental to our team. All contributors and AI assistants working on this repository must adhere to the [AI Constitution](AI_CONSTITUTION.md):

1. **Strict PII Protection**: No personally identifiable information (full names, home addresses, phone numbers, schools) for minor team members.
2. **Youth Safety**: 100% age-appropriate materials adhering to FIRST Core Values.
3. **Public & Positive Presentation**: Respectful, constructive language representing all members and partners responsibly.

---

## 📁 Repository Layout

```
FLL_76265_2026_BIOGLOW/
├── README.md                  # This file: repository overview & guidelines
├── AI_CONSTITUTION.md         # Privacy, safety, and AI collaboration policy
├── mkdocs.yml                 # Material for MkDocs documentation portal configuration
│
├── code/                      # Robot Programs & Scripts
│   ├── common/                # Shared routines (gyro drivebase, line followers, attachment helpers)
│   └── missions/              # Mission-specific programs (LEGO SPIKE Scratch)
│
└── doc/                       # Primary Documentation Hub (Compiled by MkDocs)
    ├── index.md               # Website homepage & quick navigation
    ├── guides/
    │   └── how_to_update_docs.md # Kid-friendly tutorial: how to write in Markdown & auto-publish
    ├── notes/
    │   └── missions/          # Mission breakdowns, field pathing, and scoring strategy
    ├── webtools/              # Interactive HTML/JS tools (Timer & Scoring Calculator)
    ├── blog/                  # Markdown posts capturing team milestones & updates
    ├── ideas/                 # Innovation project brainstorming & robot mechanism concepts
    ├── journal/               # Meeting notes, decision logs, and engineering notebook records
    ├── responsibilities/      # Job roles matrix and member task tracking
    ├── marketing/             # Team branding, outreach, flyer & download QR sheets
    ├── presentations/         # Presentation decks, SPIKE App setup guide & judging scripts
    └── mentors/               # Coach strategies & meeting agendas
```

---

## 🛠️ Folder Guide

### 🤖 Code (`code/`)
- **`code/common/`**: Modular, reusable helper routines written in LEGO SPIKE Scratch format. Includes gyro-assisted straight driving, line squaring, and attachment motor controllers.
- **`code/missions/`**: Organized by run sequence or mission number for clear field execution.

### 📚 Documentation (`doc/`)
- **`doc/index.md`**: Main homepage for the live documentation portal.
- **`doc/guides/how_to_update_docs.md`**: [Student Guide on Updating Documentation](doc/guides/how_to_update_docs.md) — How kids write notes in Markdown and how GitHub Actions translates them into web pages.
- **`doc/journal/`**: Dated logs from each team meetup detailing goals set, testing results, and next steps.
- **`doc/notes/missions/`**: Detailed analysis of table missions, point values, risk levels, and mechanical requirements.
- **`doc/webtools/`**: Web applications (interactive 2:30 match timer and mission scoring calculator).
- **`doc/ideas/`**: Repository for brainstorming, mechanism sketches, and innovation research.
- **`doc/responsibilities/`**: Role assignments and task status board.
- **`doc/marketing/`**: Team identity assets, flyers, community outreach materials, and sponsorship letters.
- **`doc/presentations/`**: Slide decks, outlines, and speaking scripts for judging sessions.

---

## 🌐 Automated GitHub Pages Publishing

Whenever students or coaches commit changes to Markdown files in `doc/`:
1. **GitHub Actions** automatically runs the `.github/workflows/deploy-pages.yml` workflow.
2. It compiles all Markdown notes using **Material for MkDocs** into a responsive, searchable website.
3. The site is deployed live to:  
   👉 **`https://jaimeyu.github.io/FLL_76265_2026_BIOGLOW/`**

For full instructions, read our [Student Guide on Updating Documentation](doc/guides/how_to_update_docs.md).

---

## 🔒 Security & Privacy Safeguards

This repository strictly enforces the team [AI Constitution & Safety Policy](file:///Users/jyu/Projects/FLL/FLL_76265_2026_BIOGLOW/AI_CONSTITUTION.md) to prevent credential leaks, CVE vulnerabilities, and minor PII exposure.

### Local Pre-commit Hook Setup
To activate local pre-commit checks before making commits:
```bash
./scripts/install-hooks.sh
```
Or if using `pre-commit`:
```bash
pre-commit install
```

### Security Scans Performed
1. **PII Leak Scan** (`scripts/pii_leak_scanner.py`): Scans for emails, phone numbers, SSNs, credit cards, and addresses against an exception list (`.pii-exceptions.json`).
2. **Credential & Secret Scan** (`Gitleaks`): Detects accidental API key or private token commits.
3. **CVE Vulnerability Scan** (`Trivy`): Scans dependencies and files for high/critical vulnerabilities.
4. **CI Enforcement**: All scans automatically run on GitHub Actions via `.github/workflows/security-scan.yml`.

---

## 🤝 FIRST Core Values

> **Discovery** • **Innovation** • **Impact** • **Inclusion** • **Teamwork** • **Fun**

*Gracious Professionalism*® is a way of doing things that encourages high-quality work, emphasizes the value of others, and respects individuals and the community.


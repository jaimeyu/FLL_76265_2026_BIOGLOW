# FLL Team 76265 — 2026 BIOGLOW

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
│
├── code/                      # Robot Programs & Scripts
│   ├── common/                # Shared routines (gyro drivebase, line followers, attachment helpers)
│   └── missions/              # Mission-specific programs (LEGO SPIKE Scratch / MicroPython)
│
└── doc/                       # Primary Documentation Hub
    ├── notes/
    │   └── missions/          # Mission breakdowns, field pathing, and scoring strategy
    ├── webtools/              # Interactive HTML/JS tools (published via GitHub Pages)
    ├── blog/                  # Markdown posts capturing team milestones & updates
    ├── ideas/                 # Innovation project brainstorming & robot mechanism concepts
    ├── journal/               # Meeting notes, decision logs, and engineering notebook records
    ├── responsibilities/      # Job roles matrix and member task tracking
    ├── marketing/             # Team branding, logo design, outreach & sponsor relations
    └── presentations/         # Innovation Project decks & Robot Design judging scripts
```

---

## 🛠️ Folder Guide

### 🤖 Code (`code/`)
- **`code/common/`**: Modular, reusable helper routines written in LEGO SPIKE Scratch format (or exported MicroPython scripts). Includes gyro-assisted straight driving, line squaring, and attachment motor controllers.
- **`code/missions/`**: Organized by run sequence or mission number for clear field execution.

### 📚 Documentation (`doc/`)
- **`doc/notes/missions/`**: Detailed analysis of table missions, point values, risk levels, and mechanical requirements.
- **`doc/webtools/`**: Web applications (e.g., mission timers, score calculators, strategy maps) designed to be hosted directly on **GitHub Pages**.
- **`doc/blog/`**: Progress updates and reflection posts written in Markdown.
- **`doc/ideas/`**: Repository for wild ideas, mechanism designs, and project innovations before formal selection.
- **`doc/journal/`**: Dated logs from each team meetup detailing goals set, testing results, and next steps.
- **`doc/responsibilities/`**: Role assignments (e.g., Project Lead, Hardware Lead, Software Lead, Strategy Lead) and task status.
- **`doc/marketing/`**: Team identity assets, flyers, community outreach materials, and sponsorship letters.
- **`doc/presentations/`**: Slide decks, outlines, and speaking scripts for judging sessions (Robot Design & Innovation Project).

---

## 🌐 GitHub Pages Setup (`doc/webtools/` / `doc/webutils/`)

To publish and host the web applications in `doc/webtools/`:
1. Go to repository **Settings** on GitHub.
2. Select **Pages** from the sidebar.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Pushes to the `main` branch will automatically trigger `.github/workflows/deploy-pages.yml` to publish the web tools to `https://<username>.github.io/FLL_76265_2026_BIOGLOW/`.

---

## 🤝 FIRST Core Values

> **Discovery** • **Innovation** • **Impact** • **Inclusion** • **Teamwork** • **Fun**

*Gracious Professionalism*® is a way of doing things that encourages high-quality work, emphasizes the value of others, and respects individuals and the community.

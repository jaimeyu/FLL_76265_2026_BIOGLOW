# Web Tools & GitHub Pages (`doc/webtools/` / `doc/webutils/`)

This directory contains interactive web applications and utilities designed to be hosted via GitHub Pages for FLL Team 76265. Note: `doc/webutils` is configured as a symlink alias to `doc/webtools`.

## Included Tools
- **`index.html`**: Master web dashboard featuring an interactive 2:30 match timer and resource navigation hub.
- **`bioglow_calculator.html`**: Interactive mission scoring calculator for practice runs.

## GitHub Pages Deployment
1. Navigate to **Settings** > **Pages** on GitHub.
2. Select **Source**: **GitHub Actions**.
3. The `.github/workflows/deploy-pages.yml` workflow automatically publishes this directory on every push to `main`.
4. The site will be published at `https://<username>.github.io/FLL_76265_2026_BIOGLOW/`.

## Planned Tools
- **Run Sequencer**: Drag-and-drop tool to arrange runs and calculate total estimated time.


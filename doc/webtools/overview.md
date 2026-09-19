# Web Tools & GitHub Pages (`doc/webtools/` / `doc/webutils/`)

This directory contains interactive web applications and utilities designed to be hosted via GitHub Pages for FLL Team 76265. Note: `doc/webutils` is configured as a symlink alias to `doc/webtools`.

## Included Tools
- **`index.html`**: Master web dashboard featuring an interactive 2:30 match timer and resource navigation hub.
- **`bioglow_calculator.html`**: Interactive mission scoring calculator for practice runs.
- **`mission_cad_studio.html`**: Interactive 3D Robot & Attachment CAD Studio with mouse/keyboard controls, LEGO parts catalog drawer, extensible LDraw (`.ldr`) and JSON import/export, and 1-click snapshot-to-flyer printing.


## GitHub Pages Deployment
1. Navigate to **Settings** > **Pages** on GitHub.
2. Select **Source**: **GitHub Actions**.
3. The `.github/workflows/deploy-pages.yml` workflow automatically publishes this directory on every push to `main`.
4. The site will be published at `https://<username>.github.io/FLL_76265_2026_BIOGLOW/`.

## Planned Tools
- **Run Sequencer**: Drag-and-drop tool to arrange runs and calculate total estimated time.

---

## ⚖️ Open Source Licenses & Trademark Attributions

All third-party libraries and specifications used by our web tools are 100% permissive open-source assets fully compatible with this repository's GPLv3 license:

* **Three.js, OrbitControls & TransformControls**: Licensed under the [MIT License](https://github.com/mrdoob/three.js/blob/dev/LICENSE) (Copyright &copy; 2010-2026 Three.js authors).
* **html2canvas**: Licensed under the [MIT License](https://github.com/niklasvh/html2canvas/blob/master/LICENSE) (Copyright &copy; 2012 Niklas von Hertzen).
* **Google Fonts (`Outfit`, `Space Grotesk`)**: Licensed under the [SIL Open Font License 1.1](https://openfontlicense.org/).
* **LDraw™ Standard & Specification**: Implements the open [LDraw File Format specification](https://www.ldraw.org/) (CCAL 2.0).
* **Trademark Disclaimer**: LEGO®, SPIKE™, and TECHNIC™ are trademarks of the LEGO Group of companies. FIRST® and FIRST® LEGO® League are trademarks of FIRST and the LEGO Group. These tools are non-commercial educational tools developed independently by and for FLL Team #76265 BIOGLOW under fair use, and are not sponsored, authorized, or endorsed by the LEGO Group or FIRST.


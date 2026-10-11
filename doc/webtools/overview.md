# Web Tools & GitHub Pages (`doc/webtools/` / `doc/webutils/`) — Lego Legends

This directory contains interactive web applications and utilities designed to be hosted via GitHub Pages for FLL Team #76265 **Lego Legends**. Note: `doc/webutils` is configured as a symlink alias to `doc/webtools`.

## Included Tools

### 🎮 3D Robot Simulator (`fll-sim`)
* **Live App:** [https://jaimeyu.github.io/fll_sim/](https://jaimeyu.github.io/fll_sim/)
* **Platform:** Zero-install WebGL & WebAssembly (Chrome, Safari, Edge, Firefox on laptops and Chromebooks).
* **Physics Engine:** Rapier3D Wasm running at 60 Hz with compound pin clustering.
* **Programming:** Authentic LEGO® SPIKE™ Prime Word Blocks Studio & Async Python Runtime (`PrimeHub`, `MotorPair`, `ColorSensor`).

![FLL Robot Simulator Workspace](../assets/images/simulator/01_overview.png)

#### Key Simulator Features:
1. **Top-Down & 3D Isometric Viewports**: Switch instantly between a 2D top-down alignment camera for programming and an isometric 3D orbit camera for testing attachment clearing.
2. **Dockable Telemetry & Diagnostics**: Real-time sensor readouts (Color Sensors C & D with RGB swatches and light meters, Ultrasonic Distance, 6-Axis Gyro IMU, Mat Coordinates) and motor telemetry (Ports A–F speed %, °/s, RPM, encoder angles) that dock to the bottom or right, or minimize to a compact bar.
3. **SPIKE Prime Word Blocks Studio**: Full-screen popout modal with 3-column layout (LEGO category sidebar, block palette drawer, canvas with zoom controls), autosave, zip multi-script backup, and Python toggle.
4. **Robot Architecture & Port Matrix**: Choose between DroidBot-E (Advance Driving Base) and Compact SPIKE Base, or remap motor and sensor ports to match your physical robot.
5. **3D CAD Model Inspector & Digital Twin Validator**: Load BrickLink Studio (`.io`) or LDraw (`.ldr`) files, inspect 3D geometry and kinematics, verify topological pin clustering (130+ parts clustered into rigid bodies), and test mechanisms with the virtual mouse grab hand and Technic push bar.

| Word Blocks Studio | CAD Model Inspector |
|:---:|:---:|
| ![Word Blocks Studio](../assets/images/simulator/08_spike_word_blocks_modal.png) | ![CAD Model Inspector](../assets/images/simulator/10_cad_inspector_robot.png) |

---

### ⏱️ Match Timer & Resources (`index.html`)
Master web dashboard featuring an interactive 2:30 match timer and resource navigation hub.

### 🧮 Mission Scoring Calculator (`bioglow_calculator.html`)
Interactive mission scoring calculator for practice runs and score tracking.

### 🧊 3D Robot & Attachment CAD Studio (`mission_cad_studio.html`)
Interactive 3D Robot & Attachment CAD Studio with mouse/keyboard controls, LEGO parts catalog drawer, extensible LDraw (`.ldr`) and JSON import/export, and 1-click snapshot-to-flyer printing.


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
* **FLL 3D Challenge Mission Models (`.io`)**: 3D BrickLink Studio models of official challenge missions (Bioglow, Unearthed, Submerged, Masterpiece, Superpowered) were created and published by [Komurobo](https://komurobo.com/fll/3d-models/) (`info@komurobo.com`). Komurobo is an independent robotics community initiative and is not affiliated with FIRST® or Robotique FIRST Québec.
* **Trademark Disclaimer**: LEGO®, SPIKE™, and TECHNIC™ are trademarks of the LEGO Group of companies. FIRST® and FIRST® LEGO® League are trademarks of FIRST and the LEGO Group. These tools are non-commercial educational tools developed independently by and for FLL Team #76265 BIOGLOW under fair use, and are not sponsored, authorized, or endorsed by the LEGO Group or FIRST.


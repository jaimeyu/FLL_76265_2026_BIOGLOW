# Common Code Base (`code/common/`)

This directory holds shared, reusable code blocks and subroutines for LEGO SPIKE Prime / MicroPython.

## Planned Modules
- **`drivebase_gyro`**: Gyroscope-calibrated straight driving and precision point turns.
- **`line_follow`**: Single and dual color/light sensor line followers (proportional control).
- **`line_square`**: Squaring up on black lines to reset robot positioning on the mat.
- **`attachment_control`**: Soft acceleration and stall protection for motor attachments.

## Format Guidelines
- Programs are maintained as SPIKE Scratch exported project descriptions or MicroPython scripts.
- Ensure all custom blocks are documented with input parameters and expected unit measurements (cm, degrees, power %).

---

> [!TIP]
> **Virtual Prototyping in Simulators:**
> Before running on the physical competition mat, test and tune your gyro turn, line following, and line squaring algorithms in browser simulators like **GearsBot** or **Virtual Robotics Toolkit**. Check out our [Advanced Coding Tutorials & Simulators Guide](../../doc/guides/advanced_tutorials_and_simulators.md) for direct links, tutorials, and getting-started tips!


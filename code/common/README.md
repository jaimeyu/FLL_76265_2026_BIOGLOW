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

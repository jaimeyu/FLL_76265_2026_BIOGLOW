# Mission Programs (`code/missions/`)

This directory contains individual mission programs and complete run sequences for the 2026 BIOGLOW match mat.

## Naming Convention
- **Run Sequences**: `run_1_launch.llsp`, `run_2_launch.llsp`
- **Specific Mission Programs**: `mission_01_activation.llsp`, `mission_02_sample_return.llsp`

## Best Practices
- Every mission script should start with sensor resetting (e.g. zeroing yaw angle).
- Import shared subroutines from `code/common/`.
- Annotate each run with estimated run time (seconds) and expected max points.

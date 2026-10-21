# Robotic Car Painting Cell Simulation

**Developer:** Safa Nasrin
**Software Used:** RoboDK (macOS)
**Robot Selected:** KUKA KR 210 R3100 ultra
**Reference Vehicle:** Nissan Altima 2013 (Scaled to approx. 4800x1900x1600mm)

## Project Overview
This project demonstrates an industrial robotic painting cell simulation. The goal was to program a 6-DOF KUKA industrial robot to apply a uniform coat of paint to the exterior surfaces of a vehicle, handling complex multi-curve geometries, collision checking, and path planning.

## Technical Approach & Methodology
- **Trajectory Planning:** Utilized RoboDK's "Teach Targets on Surface" feature to generate a continuous, overlapping zigzag toolpath to ensure uniform paint coverage without sparse zones.
- **Modular Programming Architecture:** To handle the physical reach limits of the stationary robot, the painting sequence was structured into modular sub-programs (e.g., `Paint_Top`, `Paint_Side`) and executed via a seamless `Main_Paint_Sequence` controller.
- **Kinematic Optimization & Singularity Avoidance:** Positioned the vehicle frame at an optimal distance (relocated 200-300mm outward) to keep the target surfaces within the robot's "sweet spot" workspace, preventing base singularities and dead zones.
- **Tool Center Point (TCP) Orientation:** Carefully calibrated the target normal vectors. Ensured the Z-axis (Blue arrow) remained perfectly perpendicular to the car's surface and aligned the X/Y axes to prevent the 6-axis wrist from hitting joint limits or flipping during wide sweeping motions.
- **Simulation Rendering:** Integrated RoboDK's Python API (`SprayOn`) to simulate the paint particles. Optimized the linear movement (`MoveL`) speeds down to `50.0 mm/s` to ensure high-fidelity particle rendering without dropped frames in the graphics engine.

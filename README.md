# Robotic Car Painting Cell Simulation

**Developer:** Safa Nasrin  
**Software:** RoboDK (macOS)  
**Robot:** KUKA KR 210 R3100 ultra  
**Vehicle Model:** Nissan Altima 2013

## 1. Overview

This assessment involves creating a robotic car painting cell simulation using RoboDK. The goal is to simulate an industrial robot painting a car's exterior surfaces using a custom paint sprayer tool.

The simulation focuses on creating painting paths, setting the correct tool orientation, and adjusting the robot's position to achieve smooth and continuous movements across the car's hood, roof, and trunk.

## 2. Simulation Setup

- Imported the KUKA KR 210 R3100 ultra robot from the RoboDK library.
- Imported a Nissan Altima 2013 3D model and scaled it to approximately 4800 × 1900 × 1600 mm.
- Added a custom 3D paint sprayer model from Free3D and configured it as the robot's active tool (TCP).
- Positioned the vehicle in the robot's workspace to allow access to the required painting areas.

## 3. Painting Path Planning

Created a 17-target zigzag trajectory to simulate painting across the hood, roof, and trunk.

The targets were arranged to provide continuous painting passes across the vehicle's top surfaces. The painting sequence was divided into separate subprograms, such as `Paint_Top`, to organize the movements and make the program easier to manage.

## 4. Robot Configuration and Optimization

**Workspace Adjustment:**  
Adjusted the vehicle frame outward by approximately 200–300 mm to improve the robot's working position and reduce issues with reachability and problematic robot configurations.

**Tool Orientation:**  
Adjusted the target orientations to keep the sprayer's Z-axis perpendicular to the vehicle surface as closely as possible. This helped maintain the correct spray direction and reduce sudden wrist rotations during movement.

**Movement Speed:**  
Set the linear painting speed to approximately 50 mm/s to achieve smoother movements during the simulated painting process.

## 5. Python Spray Simulation

Integrated the `SprayOn` Python API functionality to simulate the paint spray effect during the robot's painting movements.

This helped demonstrate the painting process visually alongside the planned robot trajectory.

## 6. Key Outcomes

- Created a robotic painting cell using an industrial robot model.
- Configured a custom paint sprayer as the robot tool.
- Planned a 17-target painting trajectory for the car's top surfaces.
- Organized the painting sequence into subprograms.
- Improved robot positioning and tool orientation through simulation adjustments.
- Demonstrated coordinated robot movements and simulated spray effects.

## 7. Software and Resources

- **RoboDK:** Robot cell setup, simulation, and path planning
- **Python API:** Spray effect simulation
- **Free3D:** Custom 3D paint sprayer model

## Author

**Safa Nasrin**

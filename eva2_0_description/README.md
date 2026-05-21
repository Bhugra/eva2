# eva2_0_description

**Owner:** Jai Bhugra  
**Role:** Arm Control Lead

## Contents
- `urdf/eva2_0.urdf` — Complete EVA 2.0 robot URDF (base, torso, both arms, head + Kinect)

## Visualize
ros2 launch urdf_tutorial display.launch.py model:=/path/to/eva2_0_description/urdf/eva2_0.urdf

## Joint Structure
- Left arm: shoulder_pan → shoulder_lift → elbow → wrist_roll → wrist_pitch
- Right arm: mirror of left
- Head: pan → tilt → roll → kinect_link (fixed)

## Phase Status
- [x] P1-T1: URDF model complete
- [ ] P1-T2: Basic servo control node
- [ ] P4: FK node, motion planning, arm controllers




**Note:** Things shown here are subjected to change

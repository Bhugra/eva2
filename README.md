# EVA 2.0 - Educational Versatile Assistant

## 🤖 Project Overview

**EVA 2.0** is a semi-humanoid educational robotics platform designed for university robotics laboratory education and live concept demonstration. EVA is not a research robot chasing the cutting edge of hardware — she is a teaching tool, crafted to make abstract robotics principles tangible, interactive, and exciting for students who learn best by doing.

### The Vision

> *"To create an accessible, modular, and educationally rich semi-humanoid robot that demonstrates core robotics concepts through practical implementation, serving as a platform for hands-on learning in university robotics laboratories."*

---

## ✨ Core Capabilities

EVA 2.0 converges six core engineering domains:

| Domain | Capabilities |
|--------|--------------|
| **Perception** | Depth sensing, RGB vision, laser scan emulation, person tracking |
| **Arm Manipulation** | Joint-level servo control, forward kinematics, smooth motion planning |
| **Locomotion** | Omnidirectional movement, PID velocity control, encoder-based odometry |
| **Navigation** | SLAM mapping, Nav2 path planning, waypoint following, visual odometry |
| **Human Interaction** | Voice commands, WebRTC web interface, touch-screen buttons |
| **Social Features** | Gender recognition, facial expression display, gesture recognition, face ID |

---

## 🏗️ Physical Configuration

- **Upper Body**: Humanoid with 2 articulated arms (5-6 DOF each), head with Kinect 360 camera
- **Lower Body**: 4 omnidirectional wheels in 90° offset configuration
- **Sensor Suite**: Microsoft Kinect 360 (RGB + Depth + 4-mic array)
- **Main Controller**: Raspberry Pi 4/5 or x86 SBC running Ubuntu 22.04/24.04
- **Actuation**: Digital servo motors (arms/head), DC geared motors (wheels with encoders)

---

## 🛠️ Technical Stack

| Layer | Technology | Version |
|-------|------------|---------|
| **OS** | Ubuntu Linux | 22.04 (Jammy) or 24.04 (Noble) |
| **Robot Middleware** | ROS2 | Jazzy Jalisco (LTS) |
| **Navigation Stack** | Nav2 | Latest stable |
| **Mapping** | SLAM Toolbox | Latest stable |
| **Vision Library** | OpenCV | 4.x |
| **Face Recognition** | face_recognition / dlib | Python wrappers |
| **Voice Assistant** | Detroit | Pre-configured |
| **Web Interface** | WebRTC | Standard browser-compatible |
| **Build System** | colcon | Standard ROS2 |

---

## 👥 Team Structure

| Name | Role | Responsibility Area | Key Initials |
|------|------|---------------------|--------------|
| **Jaideep Chouhan** | System Architect & Nav Lead | Architecture, Nav2, HMI, Integration | JC |
| **Jai Bhugra** | 3D Modelling & Arm Lead | URDF, Forward Kinematics, Motion Planning | JB |
| **Vishwajeet Singh** | Motor Control Lead | PID, Odometry, Sensor Integration, Audio | VS |
| **Vaagish** | CV Lead (Gesture & Tracking) | Hand Gesture, Person Tracking, Visual Servoing | VA |
| **Mohit** | CV Lead (Face) | Face Recognition, Expression, Gender Recognition | MH |

---

## 📋 Development Phases

The project is structured into **8 distinct phases**, each with clear deliverables and exit criteria:

### Phase Overview

```
Foundation → Perception → Locomotion → Arm Control
                                          ↓
                    ← ← ← ← Navigation ← ← 
                    ↓
                   HMI → Integration → Polish & Demo
```

### Phase Breakdown

1. **Phase 1: Foundation & Base Bring-Up**
   - Robot URDF model, basic servo control, motor bring-up, Kinect verification

2. **Phase 2: Perception & Vision Nodes**
   - Face recognition, gender classification, expression recognition, hand gesture detection

3. **Phase 3: Locomotion & Motor Control**
   - Omnidirectional kinematics, PID velocity control, odometry, wheel calibration

4. **Phase 4: Arm Manipulation & Motion Planning**
   - Forward kinematics, motion planning, arm controllers, A* demonstration

5. **Phase 5: Navigation & Mapping**
   - SLAM Toolbox integration, Nav2 configuration, visual odometry, waypoint following

6. **Phase 6: Human-Machine Interface**
   - WebRTC bridge, voice assistant integration, touch button UI, unified HMI

7. **Phase 7: Orchestration & Integration**
   - Central control node, cross-node validation, unified launch files, error handling

8. **Phase 8: Polish & Demonstration**
   - Performance optimization, refinement, demonstration scripts, documentation

---

## 📡 ROS2 Topic Naming Convention

All topics follow this hierarchical pattern:

```
/eva2_0/[subsystem]/[data_type]
```

**Approved subsystem identifiers:**
- `kinect` — Kinect sensor outputs
- `cv` — Computer vision results
- `gesture` — Hand gesture recognition
- `tracking` — Person and object tracking
- `left_arm` / `right_arm` — Arm control
- `head` — Head pan/tilt/roll
- `motors` — Wheel motor outputs
- `navigation` — Navigation commands
- `sound` — Audio/speaker direction
- `touch` — Physical touch detection
- `web` — WebRTC commands
- `voice` — Voice assistant
- `pid` — PID diagnostics
- `odometry` — Odometry data
- `vo` — Visual odometry

---

## 🚀 Quick Start

### Prerequisites
- Ubuntu 22.04 or 24.04
- ROS2 Jazzy Jalisco installed
- Python 3.10+
- Git

### Installation (Placeholder)

```bash
# Clone the repository
git clone https://github.com/[org]/eva2.git
cd eva2

# Create colcon workspace
mkdir -p ~/eva2_ws/src
cp -r eva2 ~/eva2_ws/src/

# Build all packages
cd ~/eva2_ws
colcon build

# Source the workspace
source install/setup.bash

# Launch the complete system
ros2 launch eva2_0 complete.launch.py
```

---

## 📦 Project Structure

```
eva2/
├── README.md                          # This file
├── docs/                              # Project documentation
│   ├── EVA2_0_PROJECT_HANDBOOK.pdf   # Full technical handbook
│   ├── ARCHITECTURE.md               # System architecture details
│   └── NODE_INTERFACES.md            # ROS2 node specifications
├── src/                              # ROS2 package source code
│   ├── eva2_0_control_node/          # Central orchestration
│   ├── eva2_0_face_recognition/      # Face recognition node
│   ├── eva2_0_expression_recognition/ # Emotion classifier
│   ├── eva2_0_gender_recognition/    # Gender classifier
│   ├── eva2_0_hand_gesture/          # Hand gesture recognition
│   ├── eva2_0_person_tracking/       # Person tracking node
│   ├── eva2_0_fk_node/               # Forward kinematics
│   ├── eva2_0_arm_planner/           # Motion planning
│   ├── eva2_0_pid_control/           # Motor PID controller
│   ├── eva2_0_odometry/              # Odometry publisher
│   ├── eva2_0_ear_sensor/            # Speaker direction (extra)
│   ├── eva2_0_stall_sensor/          # Touch via current sensing (extra)
│   ├── eva2_0_visual_odometry/       # Visual odometry node
│   ├── eva2_0_webrtc_bridge/         # Web interface
│   ├── eva2_0_voice_bridge/          # Voice command bridge
│   └── eva2_0_touch_ui/              # Touch button interface
├── config/                           # Configuration files
│   ├── nav_params.yaml               # Nav2 parameters
│   ├── slam_params.yaml              # SLAM configuration
│   └── [subsystem]_params.yaml       # Subsystem configs
├── launch/                           # ROS2 launch files
│   ├── complete.launch.py            # Master launch (all nodes)
│   ├── kinect_launch.py              # Sensor bring-up
│   ├── perception_launch.py          # All CV nodes
│   ├── navigation_launch.py          # Nav2 + SLAM
│   ├── hmi_launch.py                 # All interfaces
│   └── [subsystem]_launch.py         # Individual subsystems
├── models/                           # URDF models and meshes
│   ├── eva2_0.urdf.xacro            # Main URDF
│   ├── meshes/                       # Visual mesh files
│   └── [component].urdf.xacro        # Sub-component models
├── test/                             # Unit and integration tests
│   ├── test_*.py                     # Python unit tests
│   ├── test_bags/                    # Pre-recorded ROS2 bags
│   └── fixtures/                     # Test fixtures
└── scripts/                          # Utility scripts
    ├── calibrate_wheels.py           # Encoder calibration
    ├── record_test_data.py           # Record sensor data
    └── [utility_name].py             # Other utilities
```

---

## 🎯 Key Node Interfaces

### Perception Nodes
- **kinect_ros2**: Kinect sensor driver → RGB, Depth, LaserScan at 30 Hz
- **eva2_0_face_recognition**: Face detection + ID → `/eva2_0/cv/face_recognitions`
- **eva2_0_expression_recognition**: Emotion classification → `/eva2_0/cv/expression`
- **eva2_0_hand_gesture**: Hand tracking → `/eva2_0/gesture/recognized`
- **eva2_0_person_tracking**: Primary speaker ID → `/eva2_0/tracking/primary_speaker`

### Locomotion Nodes
- **eva2_0_pid_control**: Wheel velocity PID → `/eva2_0/motors/pwm_commands`
- **eva2_0_odometry**: Encoder integration → `/odom` and `/tf`
- **eva2_0_ear_sensor** (Extra): Speaker direction → `/eva2_0/sound/speaker_direction`

### Arm Control Nodes
- **eva2_0_fk_node**: Forward kinematics → `/eva2_0/left_arm/end_effector_pose`
- **eva2_0_arm_planner**: Motion planning → Action server `/eva2_0/left_arm/move_to_pose`

### Navigation Nodes
- **slam_toolbox**: SLAM mapping → `/map` at 5 Hz
- **nav2**: Path planning & control → `/cmd_vel` @ 20 Hz
- **eva2_0_visual_odometry**: Visual pose estimation (secondary)

### HMI Nodes
- **eva2_0_webrtc_bridge**: Web interface → localhost:8080
- **eva2_0_voice_bridge**: Voice commands → `/eva2_0/voice/command`
- **eva2_0_touch_ui**: Touch buttons → `/eva2_0/touch/button_press`

### Central Control
- **eva2_0_control_node**: Orchestrates all subsystems, manages state machine

---

## 📊 System State Machine

EVA operates in one of **9 defined states**:

```
INIT → IDLE ↔ PERCEIVE
       ↓ ↑ ↑   ↓
       NAVIGATE (← can go to any state)
       MANIPULATE
       INTERACT
       CHARGING
       ERROR
       
EMERGENCY_STOP ← (From any state, always)
```

**Emergency Stop Rule**: Any state can transition to `EMERGENCY_STOP` at any time. Only valid transition from `EMERGENCY_STOP` is back to `IDLE` after manual reset.

---

## 🔧 Integration Guidelines

### Topic Naming
- **Non-negotiable**: Every topic must follow `/eva2_0/[subsystem]/[data_type]` pattern
- New topics must be discussed in weekly sync and added to documentation before use

### Message Standards
- All custom messages must include `std_msgs/Header` where timestamps matter
- Include `frame_id` for pose/transform messages
- Use standard ROS2 message types where possible

### Launch File Organization
Master launch file: `complete.launch.py`
```bash
ros2 launch eva2_0 complete.launch.py
```
This single command must start **every node** without errors.

### QoS Settings
- **Perception topics**: `SENSOR` (best effort, low latency)
- **Critical commands**: `RELIABLE` (guaranteed delivery)
- **State updates**: `TRANSIENT_LOCAL` (retain last message for new subscribers)

---

## 📈 Performance Targets

| Metric | Target |
|--------|--------|
| Command-to-action latency | < 200 ms |
| Vision pipeline frame rate | > 15 FPS |
| Motor control loop frequency | 50-100 Hz |
| Odometry update rate | 30 Hz |
| SLAM map update rate | 5 Hz |
| CPU usage (idle) | < 30% |
| CPU usage (full operation) | < 80% |
| Total memory usage | < 2 GB |
| Emergency stop latency | < 100 ms |

---

## 🧪 Testing & Validation

### Required Testing
- **Unit Tests**: ≥ 70% code coverage (pytest for Python, gtest for C++)
- **Mock Interfaces**: All nodes must support isolated testing
- **Bag Recordings**: Recorded ROS2 bags in `test/test_bags/` for regression testing

### Pre-Demonstration Validation Checklist
- ✓ All nodes start without errors
- ✓ All expected topics publishing valid data
- ✓ RViz displays robot model with live joint states
- ✓ Navigation: straight-line accuracy < 0.5 m over 10 m
- ✓ Mapping: < 5% error on 10×10 m area
- ✓ Arms: 100 continuous cycles without servo failure
- ✓ Emergency stop: responds within 100 ms
- ✓ Battery: minimum 2 hours under normal operation

---

## 📚 Documentation

### Full Technical Handbook
The complete project handbook is in `docs/EVA2_0_PROJECT_HANDBOOK.pdf` (or equivalent .tex source)

### Quick References
- [ROS2 Jazzy Commands](docs/ROS2_REFERENCE.md)
- [Node Interface Specifications](docs/NODE_INTERFACES.md)
- [System Architecture](docs/ARCHITECTURE.md)
- [Development Workflow](docs/DEVELOPMENT_WORKFLOW.md)

---

## 📞 Communication & Meetings

### Weekly Team Sync
- **When**: [To be scheduled]
- **Duration**: 30 minutes
- **Agenda**: 
  - Individual progress updates (2 min each)
  - Blockers and dependencies
  - Integration status
  - Next week targets
  - Open discussion

### Communication Matrix
See detailed topic/node communication table in full handbook.

---

## 🎓 Educational Value

EVA 2.0 is designed to teach:
- **Kinematics & Control**: Forward kinematics, PID controllers, trajectory planning
- **Computer Vision**: Face detection, emotion recognition, gesture recognition
- **Robot Localization**: Odometry, SLAM, visual odometry fusion
- **Path Planning**: Nav2, obstacle avoidance, waypoint navigation
- **ROS2 Architecture**: Multi-node systems, topic/service/action patterns, launch files
- **Hardware Integration**: Sensor fusion, motor control, servo interfacing

---

## ⚠️ Safety Notes

1. **Emergency Stop**: Available from all three interfaces (web, voice, touch)
2. **Motor Stall Detection**: Servos stop immediately on physical contact
3. **Watchdog Timers**: Prevent runaway motion if control node crashes
4. **Battery Safety**: Automatic return-to-dock alert at 15% capacity
5. **Collision Avoidance**: Nav2 costmaps prevent obstacles

---

## 📝 License & Attribution

**EVA 2.0 Project**
- Version 2.0 — Production Release
- Lead Developer: Jaideep Chouhan
- Development Team: Jai Bhugra, Vishwajeet Singh, Vaagish, Mohit
- Robotics Laboratory — Semi-Humanoid Platform Division

---

## 🚀 Getting Help

- **Technical Issues**: Raise an issue on the repository with logs from `ros2 run rqt_console rqt_console`
- **Integration Questions**: Ask in weekly team sync or contact Jaideep (System Architect)
- **Debug Help**: Check the full handbook appendix for recommended debugging tools per role

---

## 📖 Repository Structure & Next Steps

1. **Read** the full project handbook in `docs/`
2. **Understand** your role and responsibilities
3. **Follow** the naming conventions and integration guidelines
4. **Test** your node before submitting a pull request
5. **Document** any new topics/parameters
6. **Review** code changes before merging to main branch

---

**Last Updated**: May 2025  
**Status**: Active Development - Phase 1 Initialization  
**Current Focus**: Hardware bring-up and base architecture

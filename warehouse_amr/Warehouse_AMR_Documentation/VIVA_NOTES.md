# Viva / Explanation Notes

## What Is This Project?

This is an Autonomous Mobile Robot for warehouse navigation. It is built using ROS 2 Humble, Gazebo, SLAM Toolbox, and Nav2. The robot can map a warehouse, save the map, localize itself, avoid obstacles, and perform pickup-drop tasks.

## Why ROS 2?

ROS 2 is used because it supports modular robot software development. Each function runs as a separate node, such as LiDAR sensing, odometry, mapping, localization, planning, and control.

## Why Gazebo?

Gazebo provides a 3D simulation environment. It allows testing the robot without real hardware. The warehouse, robot, LiDAR, and moving obstacle are simulated in Gazebo.

## What Is URDF?

URDF is used to describe the robot model. It defines robot links, joints, wheels, body, sensors, collision geometry, and inertial properties.

## What Is Xacro?

Xacro is a macro format for URDF. It allows variables such as wheel radius, robot dimensions, and sensor size, making the robot model easier to modify.

## What Is SLAM?

SLAM means Simultaneous Localization and Mapping. During SLAM, the robot uses LiDAR and odometry to build a map while estimating its own position.

## What Is Nav2?

Nav2 is the ROS 2 navigation stack. It provides localization, path planning, obstacle avoidance, behavior management, and velocity commands for autonomous movement.

## What Is AMCL?

AMCL is Adaptive Monte Carlo Localization. It estimates the robot pose on a saved map using LiDAR scan data and odometry.

## Why Initial Pose Is Needed?

The robot needs to know where it starts on the saved map. The `2D Pose Estimate` tool in RViz gives this initial pose to AMCL.

## What Is Costmap?

A costmap is a safety map used by Nav2. It marks obstacles and danger zones. Nav2 uses costmaps to plan safe paths.

There are two costmaps:

- Global costmap: used for full path planning.
- Local costmap: used for live obstacle avoidance around the robot.

## How Does the Robot Avoid Moving Obstacles?

The moving obstacle is detected by LiDAR. The local costmap marks it as an obstacle. Nav2 then either avoids it, slows down, stops, or replans depending on the available space.

## What Is `/cmd_vel`?

`/cmd_vel` is the velocity command topic. Nav2 publishes velocity commands on this topic. In simulation, the Gazebo differential drive plugin uses this topic to move the robot.

## What Is Pickup-Drop Workflow?

The pickup-drop node sends two navigation goals to Nav2:

1. Go to pickup location.
2. Wait for loading.
3. Go to drop location.
4. Finish task.

This simulates an industrial warehouse AMR task.

## How Is This Related to Real Robots?

The same high-level ROS 2 architecture can be used on real robots. Gazebo is replaced by real hardware drivers:

- Real LiDAR publishes `/scan`.
- Real motor driver receives `/cmd_vel`.
- Real odometry publishes `/odom`.
- Nav2 performs planning and control.

## Why Not Only Use YOLO?

YOLO can identify objects like humans or forklifts, but navigation needs obstacle position in the robot/world frame. LiDAR and costmaps are more direct for obstacle avoidance. YOLO can be added later as a semantic perception layer.

## Final One-Minute Explanation

This project simulates a warehouse AMR using ROS 2. I created a custom differential drive robot with LiDAR in URDF/Xacro and spawned it in a custom Gazebo warehouse world. I used SLAM Toolbox to generate and save a 2D warehouse map. Then I configured Nav2 with AMCL, planner, controller, and costmaps to navigate on the saved map. A moving obstacle was added to test dynamic obstacle detection through LiDAR and local costmaps. Finally, I created a Python action client that takes pickup and drop station names from the user and sends navigation goals automatically. This represents a real industrial AMR workflow used in warehouses.

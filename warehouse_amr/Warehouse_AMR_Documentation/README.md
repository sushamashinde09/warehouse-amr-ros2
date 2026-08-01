# Autonomous Mobile Robot (AMR) for Warehouse Navigation

## Project Overview

This project implements a warehouse Autonomous Mobile Robot (AMR) using ROS 2 Humble. The robot is simulated in Gazebo, visualized in RViz, and uses SLAM Toolbox and Nav2 for mapping, localization, path planning, obstacle avoidance, and autonomous pickup-drop task execution.

The project demonstrates an industrial AMR workflow:

1. Create a custom mobile robot model.
2. Simulate the robot in a warehouse environment.
3. Generate a map using LiDAR and SLAM.
4. Save and reload the warehouse map.
5. Localize the robot using AMCL.
6. Navigate autonomously using Nav2.
7. Detect moving obstacles using LiDAR and local costmaps.
8. Execute pickup-drop tasks using a Python action client.

## Tools and Packages Used

- ROS 2 Humble
- Gazebo Classic
- RViz2
- Nav2
- SLAM Toolbox
- AMCL
- Python `rclpy`
- Gazebo ROS plugins
- LiDAR `LaserScan`
- `nav2_msgs/action/NavigateToPose`

## Main ROS 2 Package

Package name:

```bash
warehouse_amr
```

Important folders:

```text
warehouse_amr/
  config/
    nav2_params.yaml
    slam_toolbox.yaml
  launch/
    display_robot.launch.py
    gazebo.launch.py
  maps/
    warehouse_map.pgm
    warehouse_map.yaml
  rviz/
    warehouse_nav.rviz
  urdf/
    warehouse_bot.urdf.xacro
  warehouse_amr/
    moving_obstacle_node.py
    pickup_drop_task_node.py
```

## Completed Features

- Custom robot URDF/Xacro model
- Differential drive motion using `/cmd_vel`
- LiDAR sensor publishing `/scan`
- Custom warehouse world with walls and shelves
- SLAM mapping using SLAM Toolbox
- Saved map generation
- Saved map loading using Nav2 map server
- AMCL localization
- Nav2 global and local costmaps
- Autonomous goal navigation
- Moving worker obstacle simulation
- Pickup-drop task automation using Python
- Saved RViz configuration

## Final Demo Run Commands

### Terminal 1: Gazebo

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 launch warehouse_amr gazebo.launch.py
```

### Terminal 2: Nav2

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=true map:=/home/sushama/amr_ws/src/warehouse_amr/maps/warehouse_map.yaml params_file:=/home/sushama/amr_ws/src/warehouse_amr/config/nav2_params.yaml
```

### Terminal 3: RViz

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
rviz2 -d ~/amr_ws/src/warehouse_amr/rviz/warehouse_nav.rviz
```

In RViz, first set the correct robot pose using:

```text
2D Pose Estimate
```

Then send a goal using:

```text
2D Goal Pose
```

### Terminal 4: Moving Obstacle

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 run warehouse_amr moving_obstacle_node
```

### Terminal 5: Pickup-Drop Task

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 run warehouse_amr pickup_drop_task_node
```

Example input:

```text
Enter pickup location: pickup_a
Enter drop location: drop_a
```

## Important ROS Topics

```text
/scan                 LiDAR scan data
/odom                 robot odometry
/cmd_vel              velocity command to robot
/map                  saved or SLAM-generated map
/tf                   dynamic transforms
/tf_static            static transforms
/amcl_pose            localized robot pose
/plan                 Nav2 global path
/local_costmap/costmap
/global_costmap/costmap
```

## System Flow

```text
Gazebo warehouse world
  -> robot sensors publish /scan and /odom
  -> SLAM Toolbox creates map during mapping phase
  -> saved map is loaded by Nav2 during navigation phase
  -> AMCL estimates robot pose
  -> Nav2 planner creates path
  -> Nav2 controller publishes /cmd_vel
  -> Gazebo robot moves
```

## Real-World Relevance

This project represents the basic workflow of industrial warehouse AMRs used in logistics and automated fulfillment centers. In a real robot, Gazebo components would be replaced by hardware drivers:

```text
Gazebo LiDAR -> real LiDAR driver
Gazebo odom -> wheel encoder/IMU odometry
Gazebo diff drive plugin -> motor controller
simulated map -> real warehouse map
```

The high-level Nav2 and pickup-drop logic can remain similar.

## Future Scope

- YOLO-based human/forklift detection
- Web dashboard for task assignment
- QR-code or AprilTag-based station identification
- Pallet attachment/detachment simulation
- Multi-robot fleet coordination
- Real robot hardware deployment

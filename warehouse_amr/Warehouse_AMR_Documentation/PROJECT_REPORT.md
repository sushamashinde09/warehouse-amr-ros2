# Project Report: Autonomous Mobile Robot for Warehouse Navigation

## 1. Introduction

Autonomous Mobile Robots are widely used in modern warehouses for moving goods, pallets, totes, and materials between storage racks, packing stations, and dispatch areas. This project builds a ROS 2 based AMR simulation that can map a warehouse, localize itself, avoid obstacles, and perform pickup-drop navigation tasks.

The project uses ROS 2 Humble, Gazebo, RViz, SLAM Toolbox, and Nav2. A custom robot model and warehouse world were created from scratch so that the complete AMR workflow can be understood at the concept and implementation level.

## 2. Aim

The aim of this project is to design and simulate an autonomous warehouse mobile robot that can:

- Navigate inside a warehouse environment.
- Generate a 2D map using LiDAR data.
- Save and reload the generated map.
- Localize itself on the saved map.
- Plan paths using Nav2.
- Avoid static and moving obstacles.
- Execute pickup and drop tasks using code.

## 3. Objectives

The main objectives are:

1. Create a custom ROS 2 package for the AMR.
2. Design a differential drive robot using URDF/Xacro.
3. Simulate the robot in Gazebo.
4. Add a LiDAR sensor and publish `/scan`.
5. Create a warehouse world with walls and shelves.
6. Use SLAM Toolbox to build a map.
7. Save the map using Nav2 map saver.
8. Configure Nav2 for autonomous navigation.
9. Add a moving obstacle representing worker or forklift traffic.
10. Create a Python node for pickup-drop task execution.

## 4. Software and Tools

The following tools and ROS 2 packages were used:

| Tool | Purpose |
| --- | --- |
| ROS 2 Humble | Main robotics middleware |
| Gazebo Classic | 3D robot simulation |
| RViz2 | Visualization and goal setting |
| SLAM Toolbox | 2D mapping |
| Nav2 | Autonomous navigation |
| AMCL | Localization on saved map |
| Python rclpy | Custom ROS 2 nodes |
| Gazebo ROS plugins | Robot movement, LiDAR, entity control |

## 5. Robot Model

The robot was created using URDF/Xacro. It contains:

- `base_link`: main robot body
- `left_wheel_link`: left wheel
- `right_wheel_link`: right wheel
- `caster_link`: front support caster
- `lidar_link`: LiDAR sensor body

The wheels are connected to the base using continuous joints. The caster and LiDAR are connected using fixed joints.

The robot uses a differential drive plugin. The plugin subscribes to `/cmd_vel` and converts velocity commands into wheel motion inside Gazebo.

## 6. Warehouse World

A custom warehouse world was created in Gazebo. It includes:

- Ground plane
- Boundary walls
- Shelf rows
- A moving worker obstacle

The shelves and walls act as static obstacles. The moving worker object is used to test dynamic obstacle handling.

## 7. LiDAR Sensor

A Gazebo ray sensor was added to the robot as a LiDAR. It publishes `sensor_msgs/msg/LaserScan` data on:

```text
/scan
```

The LiDAR is used for:

- SLAM mapping
- AMCL localization
- Local costmap obstacle detection
- Dynamic obstacle avoidance

## 8. SLAM Mapping

SLAM Toolbox was used to generate a 2D occupancy grid map of the warehouse.

During mapping:

```text
LiDAR /scan + odometry /odom -> SLAM Toolbox -> /map
```

After the warehouse was scanned, the map was saved as:

```text
warehouse_map.pgm
warehouse_map.yaml
```

The saved map is later used by Nav2 for localization and navigation.

## 9. Nav2 Navigation

Nav2 was configured using `nav2_params.yaml`. Important parameters include:

```text
map frame: map
odom frame: odom
base frame: base_link
scan topic: /scan
velocity topic: /cmd_vel
```

Nav2 components used:

- `map_server`: loads saved map
- `amcl`: estimates robot pose
- `planner_server`: creates global path
- `controller_server`: follows path
- `bt_navigator`: manages navigation behavior
- `local_costmap`: detects nearby obstacles
- `global_costmap`: represents the full map for planning

## 10. Costmap and Obstacle Avoidance

Costmaps are safety maps used by Nav2. They mark obstacles and inflate risky areas around them.

The project uses:

- Global costmap for static map-based path planning.
- Local costmap for live obstacle detection using LiDAR.

When a moving obstacle enters the robot path:

1. LiDAR detects it.
2. Local costmap marks it as an obstacle.
3. Nav2 controller tries to avoid it.
4. If the aisle is blocked, the robot stops.
5. When the obstacle moves away, the robot continues.

## 11. Pickup-Drop Task

A Python node was created to automate pickup-drop behavior. It uses the Nav2 `NavigateToPose` action.

The user enters named locations:

```text
pickup_a
drop_a
```

The node converts these names into map coordinates and sends goals to Nav2.

Workflow:

```text
Go to pickup point
Wait for loading
Go to drop point
Finish task
```

This is similar to a real industrial AMR workflow, where a task management system sends pickup and drop station names to the robot.

## 12. Real Robot Implementation

In a real robot, the high-level Nav2 and task logic can remain similar. The simulation-specific parts would be replaced by hardware drivers:

| Simulation | Real Robot |
| --- | --- |
| Gazebo world | Real warehouse |
| Gazebo LiDAR | Real LiDAR driver |
| Gazebo odometry | Wheel encoder + IMU odometry |
| Gazebo diff drive plugin | Motor controller |
| Simulated map | Real warehouse map |

The same concepts apply:

```text
LiDAR -> /scan
odometry -> /odom
Nav2 -> /cmd_vel
motor driver -> wheel motion
```

## 13. Results

The project successfully demonstrates:

- Custom robot simulation
- LiDAR-based mapping
- Saved map navigation
- AMCL localization
- Autonomous path planning
- Dynamic obstacle response
- Pickup-drop task automation

The final demo shows a warehouse robot navigating between pickup and drop locations while using Nav2 costmaps for obstacle awareness.

## 14. Limitations

- The pallet loading/unloading process is simulated using a wait time.
- The moving obstacle is represented as a box.
- The robot does not currently use YOLO or camera-based semantic detection.
- The project is simulation-based, not deployed on real hardware.

## 15. Future Scope

Future improvements include:

- YOLO-based human and forklift detection.
- Pallet attachment and detachment in Gazebo.
- Web dashboard for assigning pickup-drop tasks.
- Real LiDAR and motor driver integration.
- Multi-robot coordination.
- Automatic charging station behavior.

## 16. Conclusion

This project successfully builds a complete ROS 2 warehouse AMR simulation from scratch. It covers robot modeling, Gazebo simulation, LiDAR sensing, SLAM mapping, saved map navigation, AMCL localization, Nav2 costmaps, dynamic obstacle response, and pickup-drop task automation.

The project provides a strong foundation for understanding industrial autonomous mobile robots used in logistics and warehouse automation.

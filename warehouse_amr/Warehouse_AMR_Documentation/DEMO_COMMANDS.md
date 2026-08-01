# Demo Commands

Use these commands for the final project demo.

## 1. Stop Old Processes

```bash
pkill gzserver
pkill gzclient
pkill rviz2
```

## 2. Build Workspace

```bash
cd ~/amr_ws
source /opt/ros/humble/setup.bash
colcon build --packages-select warehouse_amr
source install/setup.bash
```

## 3. Start Gazebo

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 launch warehouse_amr gazebo.launch.py
```

## 4. Start Nav2

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=true map:=/home/sushama/amr_ws/src/warehouse_amr/maps/warehouse_map.yaml params_file:=/home/sushama/amr_ws/src/warehouse_amr/config/nav2_params.yaml
```

## 5. Start RViz

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
rviz2 -d ~/amr_ws/src/warehouse_amr/rviz/warehouse_nav.rviz
```

In RViz:

1. Set `2D Pose Estimate`.
2. Verify robot aligns with Gazebo.
3. Send `2D Goal Pose`.

## 6. Start Moving Obstacle

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 run warehouse_amr moving_obstacle_node
```

## 7. Run Pickup-Drop Task

```bash
source /opt/ros/humble/setup.bash
source ~/amr_ws/install/setup.bash
ros2 run warehouse_amr pickup_drop_task_node
```

Example:

```text
Enter pickup location: pickup_a
Enter drop location: drop_a
```

## Useful Debug Commands

### Check lifecycle states

```bash
ros2 lifecycle get /amcl
ros2 lifecycle get /planner_server
ros2 lifecycle get /controller_server
ros2 lifecycle get /bt_navigator
```

Expected:

```text
active [3]
```

### Check robot velocity

```bash
ros2 topic echo /cmd_vel
```

### Check map

```bash
ros2 topic echo /map --once
```

### Check localization

```bash
ros2 topic echo /amcl_pose --once
```

### Check transforms

```bash
ros2 run tf2_ros tf2_echo map base_link
```

### Check costmap topics

```bash
ros2 topic list | grep costmap
```

### Check moving obstacle service

```bash
ros2 service list | grep entity
```

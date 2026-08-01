import time

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose


class PickupDropTaskNode(Node):
    def __init__(self):
        super().__init__('pickup_drop_task_node')
        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

        self.locations = {
            'pickup_a': (-1.5, 0.0, 0.0, 1.0),
            'pickup_b': (-1.5, 1.2, 0.0, 1.0),
            'drop_a': (1.5, 0.0, 0.0, 1.0),
            'drop_b': (1.5, -1.2, 0.0, 1.0),
        }

        self.get_logger().info('Pickup-drop task node started')

    def create_pose(self, x, y, yaw_z, yaw_w):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0
        pose.pose.orientation.z = yaw_z
        pose.pose.orientation.w = yaw_w

        return pose

    def send_goal(self, pose_name, pose):
        self.get_logger().info(f'Waiting for Nav2 action server for {pose_name}...')
        self.action_client.wait_for_server()

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        self.get_logger().info(f'Sending goal: {pose_name}')
        send_goal_future = self.action_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error(f'Goal rejected: {pose_name}')
            return False

        self.get_logger().info(f'Goal accepted: {pose_name}')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        status = result_future.result().status
        if status == 4:
            self.get_logger().info(f'Goal reached: {pose_name}')
            return True

        self.get_logger().warn(f'Goal failed: {pose_name}, status={status}')
        return False

    def print_locations(self):
        self.get_logger().info('Available locations:')
        for name, pose in self.locations.items():
            self.get_logger().info(f'  {name}: x={pose[0]}, y={pose[1]}')

    def get_location_from_user(self, prompt):
        while True:
            location_name = input(prompt).strip().lower()
            if location_name in self.locations:
                return location_name

            print(f'Invalid location: {location_name}')
            print('Available:', ', '.join(self.locations.keys()))

    def run_task(self):
        self.print_locations()

        pickup_name = self.get_location_from_user('Enter pickup location: ')
        drop_name = self.get_location_from_user('Enter drop location: ')

        pickup_pose = self.create_pose(*self.locations[pickup_name])
        drop_pose = self.create_pose(*self.locations[drop_name])

        pickup_ok = self.send_goal(pickup_name, pickup_pose)
        if not pickup_ok:
            self.get_logger().error('Pickup failed. Stopping task.')
            return

        self.get_logger().info('Simulating loading pallet...')
        time.sleep(3.0)

        drop_ok = self.send_goal(drop_name, drop_pose)
        if not drop_ok:
            self.get_logger().error('Drop failed. Stopping task.')
            return

        self.get_logger().info('Pickup-drop task completed successfully')


def main(args=None):
    rclpy.init(args=args)
    node = PickupDropTaskNode()
    node.run_task()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

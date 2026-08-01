import math

import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SetEntityState
from gazebo_msgs.msg import EntityState
from geometry_msgs.msg import Pose, Point, Quaternion, Twist, Vector3


class MovingObstacleNode(Node):
    def __init__(self):
        super().__init__('moving_obstacle_node')

        self.client = self.create_client(SetEntityState, '/set_entity_state')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /set_entity_state service...')

        self.t = 0.0
        self.timer = self.create_timer(0.1, self.move_obstacle)

        self.get_logger().info('Moving obstacle node started')

    def move_obstacle(self):
        self.t += 0.1

        y_position = 2.2 * math.sin(0.35 * self.t)

        state = EntityState()
        state.name = 'moving_worker'
        state.reference_frame = 'world'

        state.pose = Pose(
            position=Point(x=0.0, y=y_position, z=0.6),
            orientation=Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        )

        state.twist = Twist(
            linear=Vector3(x=0.0, y=0.0, z=0.0),
            angular=Vector3(x=0.0, y=0.0, z=0.0)
        )

        request = SetEntityState.Request()
        request.state = state

        self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    node = MovingObstacleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

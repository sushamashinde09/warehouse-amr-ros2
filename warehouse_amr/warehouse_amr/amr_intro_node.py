import rclpy
from rclpy.node import Node


class AMRIntroNode(Node):
    def __init__(self):
        super().__init__('amr_intro_node')
        self.get_logger().info('Warehouse AMR node started')


def main(args=None):
    rclpy.init(args=args)
    node = AMRIntroNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

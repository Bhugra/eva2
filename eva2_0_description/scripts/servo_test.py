import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class ServoTestNode(Node):
    def __init__(self):
        super().__init__('servo_test_node')
        
        # creates a publisher on the topic
        self.publisher = self.create_publisher(
            JointState,                              # message type
            '/eva2_0/left_arm/joint_commands',       # topic name
            10                                       # queue size
        )
        
        # calls publish_command every 0.1 seconds
        self.timer = self.create_timer(0.1, self.publish_command)
        self.get_logger().info('Servo test node running...')

    def publish_command(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['left_shoulder_pan_joint']  # joint name from your URDF
        msg.position = [math.radians(45)]        # 45 degrees converted to radians
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = ServoTestNode()
    rclpy.spin(node)    # keeps node alive and running
    rclpy.shutdown()

if __name__ == '__main__':
    main()

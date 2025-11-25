#!/usr/bin/env/python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

import time


class ControlRobot(Node):
    def __init__(self):
        super().__init__("control_robot_node")

        topic_movil = "/cmd_vel"
        topic_joint0 = "/joint0/cmd_pos"
        topic_joint1 = "/joint1/cmd_pos"

        self.movil_publisher_ = self.create_publisher(Twist, topic_movil, 10)
        self.joint0_publisher_ = self.create_publisher(Float64, topic_joint0, 10)
        self.joint1_publisher_ = self.create_publisher(Float64, topic_joint1, 10)

        self.timer_ = self.create_timer(1.0, self.control_callback)
        self.get_logger().info("Nodo de control del robot móvil activado")

    def control_callback(self):
        msg_movil = Twist()
        msg_joint0 = Float64()
        msg_joint1 = Float64()

        msg_movil._linear.x = 0.2
        msg_movil._angular.z = 0.0
        msg_joint0.data = 0.0
        msg_joint1.data = 1.57

        self.movil_publisher_.publish(msg_movil)
        self.joint0_publisher_.publish(msg_joint0)
        self.joint1_publisher_.publish(msg_joint1)
        time.sleep(3)

        msg_movil = Twist()
        msg_joint0 = Float64()
        msg_joint1 = Float64()

        msg_movil._linear.x = 0.2
        msg_movil._angular.z = 0.2
        msg_joint0.data = 1.57
        msg_joint1.data = 0.0

        self.movil_publisher_.publish(msg_movil)
        self.joint0_publisher_.publish(msg_joint0)
        self.joint1_publisher_.publish(msg_joint1)
        time.sleep(3)

        msg_movil = Twist()
        msg_joint0 = Float64()
        msg_joint1 = Float64()

        msg_movil._linear.x = 0.0
        msg_movil._angular.z = 0.0
        msg_joint0.data = 0.0
        msg_joint1.data = 0.0

        self.movil_publisher_.publish(msg_movil)
        self.joint0_publisher_.publish(msg_joint0)
        self.joint1_publisher_.publish(msg_joint1)
        time.sleep(3)

def main(args=None):
    rclpy.init(args=args)
    node = ControlRobot()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

        
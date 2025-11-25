#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

import time


class ControlScara(Node):
    def __init__(self):
        super().__init__("control_scara_node")

        topic_link_joint1 = "/joint1/cmd_pos"
        topic_link_joint2 = "/joint2/cmd_pos"
        topic_link_joint3 = "/joint3/cmd_pos"

        self.joint1_publisher_ = self.create_publisher(Float64, topic_link_joint1, 10)
        self.joint2_publisher_ = self.create_publisher(Float64, topic_link_joint2, 10)
        self.joint3_publisher_ = self.create_publisher(Float64, topic_link_joint3, 10)

        self.timer_ = self.create_timer(1.0, self.control_callback)
        self.get_logger().info("Nodo de control del robot SCARA activado")

    def control_callback(self):
        msg_joint1 = Float64()
        msg_joint2 = Float64()
        msg_joint3 = Float64()

        msg_joint1.data = 0.0
        msg_joint2.data = 1.57
        msg_joint3.data = -1.57

        self.joint1_publisher_.publish(msg_joint1)
        self.joint2_publisher_.publish(msg_joint2)
        self.joint3_publisher_.publish(msg_joint3)
        time.sleep(3)

        msg_joint1 = Float64()
        msg_joint2 = Float64()
        msg_joint3 = Float64()

        msg_joint1.data = 1.57
        msg_joint2.data = 0.0
        msg_joint3.data = 2.35

        self.joint1_publisher_.publish(msg_joint1)
        self.joint2_publisher_.publish(msg_joint2)
        self.joint3_publisher_.publish(msg_joint3)
        time.sleep(3)

        msg_joint1 = Float64()
        msg_joint2 = Float64()
        msg_joint3 = Float64()

        msg_joint1.data = 0.0
        msg_joint2.data = 0.0
        msg_joint3.data = 0.0

        self.joint1_publisher_.publish(msg_joint1)
        self.joint2_publisher_.publish(msg_joint2)
        self.joint3_publisher_.publish(msg_joint3)
        time.sleep(3)

def main(args=None):
    rclpy.init(args=args)
    node = ControlScara()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

        
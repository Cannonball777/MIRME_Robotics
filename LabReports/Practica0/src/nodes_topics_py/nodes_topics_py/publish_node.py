#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from math import sin,pi

from std_msgs.msg import Float64
 

class MyPublish(Node):
  def __init__(self):
    super().__init__("publish_node")
    self.t_ = 0.0
    self.freq_ = 1
    self.publisher_ = self.create_publisher(Float64,"publish_topic_velrad", 10)
    self.get_logger().info("Nodo publicador activo")
    self.create_timer(1,self.sin_publish)

  def sin_publish(self):
    msg = Float64()
    msg.data = sin(2*pi*self.freq_*self.t_)
    self.publisher_.publish(msg)
    self.get_logger().info("La velocidad en rad/s es: " + str(msg.data))
    self.t_+=0.1
    

def main(args=None):
  rclpy.init(args=args)
  node = MyPublish()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == '__main__':
  main()
  

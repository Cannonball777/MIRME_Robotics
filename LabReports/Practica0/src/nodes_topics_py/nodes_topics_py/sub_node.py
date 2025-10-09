#!usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64



class SubNode(Node):
  def __init__(self ):
    super().__init__("node_sub")
    self.mensaje_ = 0.0
    self.subcriber_ = self.create_subscription(Float64,"publish_topic_velrad",self.sin_publish_rpm,10)
    self.vel_rpm_motor_ = self.create_publisher(Float64,"publish_topic_rpm",10)
    self.get_logger().info("Nodo subcriptor activo")

  def sin_publish_rpm(self,msg):
    self.mensaje_ = msg.data    
    self.new_msg_ = Float64()
    self.new_msg_.data = self.mensaje_*9.55
    #El valor 9.55 es el factor de conversión utilizado para pasar de rad/s a rpm
    self.vel_rpm_motor_.publish(self.new_msg_)
    self.get_logger().info("La velocidad en rpm es: "+str(self.new_msg_.data))

def main(args=None):
  rclpy.init(args=args)
  node = SubNode()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == "__main__":
  main()
  

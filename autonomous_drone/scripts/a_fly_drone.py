#!/usr/bin/env python3

####
# 
#  Written by Muhammad Luqman
# 
#  13/6/21
#
###
import rospy
import cv2 
from sensor_msgs.msg import Range 
from geometry_msgs.msg import Twist

class distance_from_ground():
  def __init__(self):
    self.subscriber = rospy.Subscriber("/sonar_height",Range,self.process_data,10)
    self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.robot_velocity = Twist()
    self.set_point=1
  

  def process_data(self,data,temp): 

    if(data.range >= 1.5):
        self.robot_velocity.linear.z=0.0
        self.velocity_publisher.publish(self.robot_velocity)
    else:
        print("Reaching set point")
        self.robot_velocity.linear.z=1.0
        self.velocity_publisher.publish(self.robot_velocity)


def main(args=None):
  rospy.init_node('MidAir_stand')
  lets_fly = distance_from_ground()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Exiting")
  
if __name__ == '__main__':
  main()
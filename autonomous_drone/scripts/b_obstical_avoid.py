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
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class obstical_avoidence():
  def __init__(self):
    self.subscriber = rospy.Subscriber("/scan",LaserScan,self.laser_data_processing,10)
    self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.robot_velocity = Twist()
    self.regions={'left':[],'mid':[],'right':[]}
    self.region_1_max=0;self.region_2_max=0;self.region_3_max=0



  def laser_data_processing(self,scan_data,temp): 
    # print(len(scan_data.ranges)) total values are 1081
    #1- Regions Splitting
    self.regions = {
        'left':   scan_data.ranges[6:354],
        'mid':     scan_data.ranges[366:714],
        'right':    scan_data.ranges[726:1075],
        }

    # print(self.regions['left']," \nmid\n ",self.regions['mid'],"\nright\n ",self.regions['right'],"\nleft\n")

    #2- Processing Regions with obsticals
      
    self.region_1_max= min(min(scan_data.ranges[6:354])   , 10 )
    self.region_2_max= min(min(scan_data.ranges[366:714])  , 10 )
    self.region_3_max= min(min(scan_data.ranges[726:1075])  , 10 )
    # print(round(self.region_1_max,3),"/",round(self.region_2_max,3) ,"/",round(self.region_3_max,3))

    if(self.region_1_max !=10 and self.region_2_max!= 10 and self.region_3_max!= 10):
      #case : 111 object is on all sides
      print("Case : 111 ")
      self.robot_velocity.linear.x=0.0
      self.robot_velocity.angular.z=0.57
      self.velocity_publisher.publish(self.robot_velocity)
    elif((self.region_1_max ==10 and self.region_2_max== 10 and self.region_3_max== 10)):
      #case : 101 No object Move Slowly
      print("Case : 000")
      self.robot_velocity.linear.x=0.02
      self.robot_velocity.angular.z=0.0
      self.velocity_publisher.publish(self.robot_velocity)
    elif((self.region_1_max !=10 and self.region_2_max== 10 and self.region_3_max!= 10)):
      #case : 101 object is on left and right
      print("Case : 101 ")
      self.robot_velocity.linear.x=0.05
      self.robot_velocity.angular.z=0.0
      self.velocity_publisher.publish(self.robot_velocity)
    elif((self.region_1_max ==10 and self.region_2_max!= 10 and self.region_3_max== 10)):
      #case : 010  object is on front only
      print("Case : 010 ")
      self.robot_velocity.linear.x=0.0
      self.robot_velocity.angular.z=0.57
      self.velocity_publisher.publish(self.robot_velocity)
    elif((self.region_1_max ==10 and self.region_2_max!= 10 and self.region_3_max!= 10)):
      #case : 011 object is on front and right
      print("Case : 011 ")
      self.robot_velocity.linear.x=0.0
      self.robot_velocity.angular.z=0.57
      self.velocity_publisher.publish(self.robot_velocity)
    elif((self.region_1_max !=10 and self.region_2_max!= 10 and self.region_3_max== 10)):
      #case : 110 object is on front and left
      print("Case : 110 ")
      self.robot_velocity.linear.x=0.0
      self.robot_velocity.angular.z=-0.57
      self.velocity_publisher.publish(self.robot_velocity)



def main(args=None):
  rospy.init_node('laser_processing')
  fly_carefully = obstical_avoidence()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Exiting")
  
if __name__ == '__main__':
  main()
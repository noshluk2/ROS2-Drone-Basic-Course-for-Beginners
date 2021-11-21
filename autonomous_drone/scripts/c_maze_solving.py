#!/usr/bin/env python3

####
# 
#  Written by Muhammad Luqman
# 
#  13/6/21
#
###
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range 
import time


class Maze_solver():
  def __init__(self):
    self.subscriber = rospy.Subscriber("/scan",LaserScan,self.process_lidar,10)
    self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.subscriber = rospy.Subscriber("/sonar_height",Range,self.process_sonar,10)
    self.robot_velocity = Twist()
    self.sonar_read=Range()
    self.regions={'left':[],'mid':[],'right':[]}
    self.region_1_max=0;self.region_2_max=0;self.region_3_max=0
    self.case="start_moving"
    self.box_bound=[0,0,0,0]

  def process_sonar(self,data,temp): 
    self.sonar_read=data.range
    
  def process_lidar(self,scan_data,temp): 
    self.regions = {
        'left':   scan_data.ranges[6:354],
        'mid':     scan_data.ranges[366:714],
        'right':    scan_data.ranges[726:1075],
        }
    self.region_1_max= min(min(scan_data.ranges[0:2])   , 10 )
    self.region_2_max= min(min(scan_data.ranges[7:10])  , 10 )
    self.region_3_max= min(min(scan_data.ranges[16:18])  , 10 ) 
    
    self.solve_maze()


  def solve_maze(self):
    print()
    if((self.region_1_max !=10 and self.region_2_max== 10 and self.region_3_max!= 10)):
      #case : 101 wall is on left and right  -> move straight forward
      print("Case :101 Straight Movement //",self.region_1_max , " / ",self.region_2_max , " / ",self.region_3_max )

      self.robot_velocity.linear.x=0.5
      self.robot_velocity.angular.z=0.0

    elif((self.region_1_max !=10 and self.region_2_max!=10 and self.region_3_max== 10)):
      print("Case :110 Right Turn // ",self.region_1_max , " / ",self.region_2_max , " / ",self.region_3_max )
      self.robot_velocity.linear.x=0.0
      self.robot_velocity.angular.z=0.-50

    elif((self.region_1_max ==10 and self.region_2_max!=10 and self.region_3_max!= 10)):
      print("Case :011 Left Turn // ", self.region_1_max , " / ",self.region_2_max , " / ",self.region_3_max )
      self.robot_velocity.linear.x=0.0
      self.robot_velocity.angular.z=0.50

    elif((self.region_1_max !=10 and self.region_2_max!=10 and self.region_3_max!= 10)):
      print("Case :111 Dead End // ",self.region_1_max , " / ",self.region_2_max , " / ",self.region_3_max )
      self.robot_velocity.linear.x=0.0
      self.robot_velocity.angular.z=0.70
    
    self.velocity_publisher.publish(self.robot_velocity)
    



    


def main(args=None):
  rospy.init_node('laser_processing')
  drone_solving_maze = Maze_solver()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Exiting")
  
if __name__ == '__main__':
  main()
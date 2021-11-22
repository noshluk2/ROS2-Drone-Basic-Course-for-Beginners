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

class obstical_avoidence():
  def __init__(self):
    self.subscriber = rospy.Subscriber("/scan",LaserScan,self.laser_data_processing,10)
    self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.robot_velocity = Twist()
    self.regions={'left': [], 'mid':[],  'right':[]    }

  def laser_data_processing(self,data,temp):
        self.regions = { 'left' : data.ranges[0:360],'mid' : data.ranges[360:720], 'right' : data.ranges[720:1081] }
        region_left_min=min( min(self.regions['left']) , 6 ) ; 
        region_mid_min = min( min(self.regions['mid']) ,6 ); 
        region_right_min=min ( min(self.regions['right']) , 6 ); 
        # print(" // ",region_left_min , "// ",region_mid_min , " // ",region_right_min)


        if(region_left_min!=6 and region_mid_min!=6 and region_right_min!=6):
              print("Case 111 : Take a U turn")
              self.robot_velocity.linear.x  = 0.0
              self.robot_velocity.angular.z = 0.8
              self.velocity_publisher.publish(self.robot_velocity)
        elif(region_left_min!=6 and region_mid_min==6 and region_right_min!=6):
              print("Case 101 : Straight Movement")
              self.robot_velocity.linear.x  = 0.5
              self.robot_velocity.angular.z = 0.0
              self.velocity_publisher.publish(self.robot_velocity)
        elif(region_left_min==6 and region_mid_min!=6 and region_right_min!=6):
              print("Case 011 : Take Left Turn")
              self.robot_velocity.linear.x  = 0.3
              self.robot_velocity.angular.z = 0.5
              self.velocity_publisher.publish(self.robot_velocity)
        elif(region_left_min!=6 and region_mid_min!=6 and region_right_min==6):
              print("Case 110 : Take Right Turn")
              self.robot_velocity.linear.x  = 0.3
              self.robot_velocity.angular.z = -0.5
              self.velocity_publisher.publish(self.robot_velocity)
        elif(region_left_min==6 and region_mid_min==6 and region_right_min!=6):
              print("Case 001 : Move Straight")
              self.robot_velocity.linear.x  = 0.5
              self.robot_velocity.angular.z = 0.0
              self.velocity_publisher.publish(self.robot_velocity)
        elif(region_left_min!=6 and region_mid_min==6 and region_right_min==6):
              print("Case 100 : Move Straight")
              self.robot_velocity.linear.x  = 0.5
              self.robot_velocity.angular.z = 0.0
              self.velocity_publisher.publish(self.robot_velocity)
        elif(region_left_min==6 and region_mid_min==6 and region_right_min==6):
              print("Case 000 : Do not Move")
              self.robot_velocity.linear.x  = 0.0
              self.robot_velocity.angular.z = 0.0
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
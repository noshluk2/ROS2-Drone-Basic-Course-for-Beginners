#!/usr/bin/env python3

####
# 
#  Written by Muhammad Luqman
# 
#  17/11/21
#
###
import rospy
import cv2 
from cv_bridge import CvBridge 
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image 
from std_msgs.msg import Float32
import time

class diamond_read_Video():
  def __init__(self):
    self.camera_subscriber = rospy.Subscriber("/front_cam/camera/image",Image,self.video_feed,10)
    self.subscriber = rospy.Subscriber("/scan",LaserScan,self.laser_data_processing,10)
    self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.error_pub = rospy.Publisher('/Error', Float32, queue_size=10)
    self.set_point = rospy.Publisher('/Lidar_output', Float32, queue_size=10)

    self.out = cv2.VideoWriter('/home/luqman/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (640,480))
    self.bridge = CvBridge() # converting ros images to opencv data
    self.robot_velocity = Twist()
    self.regions={'left':[],'mid':[],'right':[]}
    self.region_1_max=0;self.region_2_max=0;self.region_3_max=0
    self.error=0;self.pre_error=0

  def video_feed(self, data,a):
    frame = self.bridge.imgmsg_to_cv2(data,'bgr8')
    self.out.write(frame)
    cv2.imshow("output", frame) 
    cv2.waitKey(1) 

  def laser_data_processing(self,scan_data,temp): 
    self.regions = {
        'left':   scan_data.ranges[6:354],
        'mid':     scan_data.ranges[366:714],
        'right':    scan_data.ranges[726:1075],
        }
    self.region_1_max= min(min(scan_data.ranges[6:354])   , 10 )
    self.region_2_max= min(min(scan_data.ranges[366:714])  , 10 )
    self.region_3_max= min(min(scan_data.ranges[726:1075])  , 10 )
    self.robot_velocity.linear.x=0.5
    self.robot_velocity.angular.z=0.2
    self.velocity_publisher.publish(self.robot_velocity)


    
    




def main(args=None):
  rospy.init_node('diamond_guard')
  secure_it = diamond_read_Video()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Exiting")
  
if __name__ == '__main__':
  main()
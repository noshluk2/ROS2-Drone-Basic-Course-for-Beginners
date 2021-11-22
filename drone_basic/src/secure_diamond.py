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
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image 

class diamond_read_Video():
  def __init__(self):
    self.camera_subscriber = rospy.Subscriber("/front_cam/camera/image",Image,self.video_feed,10)
    self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


    self.out = cv2.VideoWriter('/home/luqman/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (640,480))
    self.bridge = CvBridge()
    self.robot_velocity = Twist()

  def video_feed(self, data,a):
    frame = self.bridge.imgmsg_to_cv2(data,'bgr8')

    frame = cv2.GaussianBlur(frame, (7, 7), 1.41)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(frame, 25, 75)
    cv2.imshow("Canny_result", edge) 

#     self.out.write(frame)
    
#     cv2.imshow("feed",frame)
    cv2.waitKey(1) 

  
def main(args=None):
  rospy.init_node('diamond_guard')
  secure_it = diamond_read_Video()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Exiting")
  
if __name__ == '__main__':
  main()
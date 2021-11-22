#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range


def talker():
    global velocity_msg , pub 
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("/sonar_height", Range, sonar_callback)
    rospy.init_node('fly_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    velocity_msg=Twist()
    rospy.spin()

def sonar_callback(msg):
    global velocity_msg , pub
    sonar_data=msg.range
    if(sonar_data>=1.5):
        velocity_msg.linear.z=0.0
        print("Reaching the Point")
    else:
        velocity_msg.linear.z=0.5
        print("Reaching set point")


    pub.publish(velocity_msg)

    print("Sonar Values : " , sonar_data) 




if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
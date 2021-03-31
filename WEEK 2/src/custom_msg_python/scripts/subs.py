#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16


def callback(data):
	rospy.loginfo("The output is %d, which is the product of (a+b), 7 ",data.data)
     
def listener():
	rospy.init_node("f_subscriber", anonymous=True)
	rospy.Subscriber("pubs", Int16, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()

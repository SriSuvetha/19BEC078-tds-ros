#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from custom_msg_python.msg import custom
 
def callback(data):
	rospy.loginfo("a=%d , b=%d", (data.a),(data.b))
	mul=(data.a+data.b)*7
	r=rospy.Rate(1)
	pub=rospy.Publisher("pubs",Int16,queue_size=1)
	pub.publish(mul)
	r.sleep()
     
def listener():
	rospy.init_node('msg_subscriber', anonymous=True)
	rospy.Subscriber("custom", custom, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()

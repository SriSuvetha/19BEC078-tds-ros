#!/usr/bin/env python  
import rospy
from std_msgs.msg import Int16
from custom_msg_python.msg import custom

def main():
   rospy.init_node("msg_publisher")
   pub = rospy.Publisher("custom", custom, queue_size=1)
   r=rospy.Rate(1)
   
   msg = custom()
   while not rospy.is_shutdown():
      msg.a = 7
      msg.b = 3
      pub.publish(msg)
      r.sleep()

if __name__ =="__main__":
   try:
      main()
   except rospy.ROSInterruptException:
      pass  


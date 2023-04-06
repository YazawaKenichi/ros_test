#!/usr/bin/env python3
# coding : utf-8
# ros_test > talker.py

import rospy
from std_msgs.msg import String

def talker():
    # Topic : chatter, Type : String, 
    pub = rospy.Publisher("chatter", String, queue_size = 10)
    # Node : talker
    rospy.init_node("talker", anonymous = True)
    # 10 Hz
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = "Hello, World! %s"%rospy.get_time()
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException: pass


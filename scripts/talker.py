#!/usr/bin/env python3
# coding : utf-8
# ros_test > talker.py

import rospy
from std_msgs.msg import String
import random

def bar(num, bar_len):
    ret = ""
    for _ in range(num):
        ret = ret + "#"
    for _ in range(bar_len - num):
        ret = ret + "-"
    return ret

def talker():
    _max = 1000
    bar_len = 50
    # Topic : chatter, Type : String, 
    pub = rospy.Publisher("chatter", String, queue_size = 10)
    # Node : talker
    rospy.init_node("talker", anonymous = True)
    # 10 Hz
    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        num = random.randrange(_max - 1)
        msg = f"{num:0>3} ["
        msg = msg + bar(int(bar_len * num / _max), bar_len) + "]"
        print(msg)
        # rospy.loginfo(str)
        pub.publish(msg)
        r.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException: pass


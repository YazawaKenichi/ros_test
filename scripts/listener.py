#!/usr/bin/env python3
# coding : utf-8
# ros_test > listener.py

import rospy
from std_msgs.msg import String

def callback(data):
    # Subscribed message are handed over in data
    print(data.data, end = "\r\n")
    # rospy.loginfo(data.data)

def listener():
    # Node : listener
    rospy.init_node("listener", anonymous = True)
    # Topic : chatter, Type : String, Callback : callback
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()


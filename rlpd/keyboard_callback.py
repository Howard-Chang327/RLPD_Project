#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def keyboard_callback(data):
    key = data.data

    if key == 'w':
        rospy.loginfo("Move forward.")
        # Add your robot's command function here to move forward
    elif key == 'a':
        rospy.loginfo("Turn left.")
        # Add your robot's command function here to turn left
    elif key == 's':
        rospy.loginfo("Move backward.")
        # Add your robot's command function here to move backward
    elif key == 'd':
        rospy.loginfo("Turn right.")
        # Add your robot's command function here to turn right
    else:
        rospy.logwarn("Unknown key.")

def listener():
    rospy.init_node('keyboard_listener')
    rospy.Subscriber('keyboard', String, keyboard_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

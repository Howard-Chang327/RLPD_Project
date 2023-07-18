#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pynput import keyboard

class KeyboardPublisher:
    def __init__(self):
        # Initialize the node
        rospy.init_node('keyboard_publisher')

        # Create publisher
        self.pub = rospy.Publisher('keyboard', String, queue_size=10)

        # Create a keyboard listener
        self.listener = keyboard.Listener(
            on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            # Respond only to 'w', 'a', 's', 'd', "h" keys
            if key.char in ['w', 'a', 's', 'd', "h"]:
                rospy.loginfo('key {0} pressed'.format(key.char))
                self.pub.publish(key.char)
        except AttributeError:
            pass

    def spin(self):
        rospy.spin()

if __name__ == "__main__":
    keyboard_publisher = KeyboardPublisher()
    keyboard_publisher.spin()

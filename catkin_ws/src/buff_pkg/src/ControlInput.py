#!/usr/bin/python3

import rospy
from std

class ControlInput(object):

    def __init__(self):
        rospy.init_node("ControlInput", anonymous=True, disable_signals=True)

        rospy.Subscriber("/music/beats", Empty )

def __main__():
    controlInput = ControlInput()
            
if __name__ == '__main__':
    __main__()
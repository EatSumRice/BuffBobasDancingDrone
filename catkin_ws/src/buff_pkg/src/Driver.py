#!/usr/bin/python3

import rospy

class Driver(object):

    def __init__(self):
        rospy.init_node("driver", anonymous=True, disable_signals=True)

def __main__():
    driverInput = DriverInput()
            
if __name__ == '__main__':
    __main__()
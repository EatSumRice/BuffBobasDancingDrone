#!/usr/bin/python3
import rospy

class MusicInput(object):

    def __init__(self):
        rospy.init_node(MusicInput, anonymous=True, disable_signals=True)

def __main__():
    musicInput = MusicInput()
            
if __name__ == '__main__':
    __main__()
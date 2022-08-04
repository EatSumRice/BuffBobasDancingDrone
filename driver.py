#!/usr/bin/env python3

from ast import FormattedValue
from djitellopy import Tello
from socket import MsgFlag
from rosdep2 import RosdepLookup
import rospy
from tello_wrapper.msg import Flip
from tello_wrapper.msg import State
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from rosgraph_msgs.msg import Clock
from sensor_msgs.msg import Image
import time
import cv2
from cv_bridge import CvBridge


class Driver(object):

    pub_state = None
    pub_camera_for = None
    pub_camera_down = None
    tello = None

    def __init__(self):

        rospy.init_node('driver', anonymous=True, disable_signals=True)

        self.pub_state = rospy.Publisher('/tello/state', State, queue_size = 10)
        self.pub_camera_for = rospy.Publisher('/tello/cam_forward', Image, queue_size = 10)
        #self.pub_camera_down = rospy.Publisher('/tello/cam_downward', Image, queue_size = 10)
        rospy.Subscriber("/tello/flip", Flip, self.flip_cb)
        rospy.Subscriber("/tello/cmd_vel", Twist, self.cmd_vel_cb)
        rospy.Subscriber("/tello/takeoff", Empty, self.takeoff_cb)
        rospy.Subscriber("/tello/land", Empty, self.land_cb)


        #host='192.168.10.1', retry_count=3
        self.tello = Tello(host='192.168.10.1', retry_count=3)
        self.tello.connect()
        self.tello.streamon()

        self.bridge = CvBridge()
        
        rospy.loginfo("Connected to drone.")

        
        
        self.rate = rospy.Rate(10)

    def flip_cb(self, msg: Flip) -> None:
        rospy.loginfo("received command: flip")
        if msg.dir == "left":
            self.tello.flip_left()
        if msg.dir == "right":
            self.tello.flip_right()
        if msg.dir == "forward":
            self.tello.flip_forward()
        if msg.dir == "backward":
            self.tello.flip_backward()

    def cmd_vel_cb(self, msg: Twist) -> None:
        rospy.loginfo("received command: move")
        if msg.linear.x > 0:
            self.tello.move_right()
        if msg.linear.x < 0:
            self.tello.move_left()
        if msg.linear.y > 0:
            self.tello.move_forward()
        if msg.linear.y < 0:
            self.tello.move_backwards() 
        if msg.linear.z > 0:
            self.tello.move_up()
        if msg.linear.z < 0:
            self.tello.move_down()

    def takeoff_cb(self, msg: Empty) -> None:
        rospy.loginfo("takeoff")
        self.tello.takeoff()
    
    def land_cb(self, msg: Empty) -> None:
        rospy.loginfo("land")
        self.tello.land()
        rospy.signal_shutdown("land command")

    def state_pub(self) -> None:
        state = State()
        state.bat = self.tello.get_battery()
        self.pub_state.publish(state)

    def cam_forward_pub(self):
        frame_read = self.tello.get_frame_read()
        frame = frame_read.frame
        frame_resize = cv2.resize(frame, (680, 540))
        image = self.bridge.cv2_to_imgmsg(frame_resize, 'rgb8')
        self.pub_camera_for.publish(image)

        

def __main__():
    driver = Driver()
    #rospy.loginfo("iter")
    while not rospy.is_shutdown():
        driver.state_pub()
        driver.cam_forward_pub()
        #time.sleep(.1)
        #rospy.loginfo("iter")
            
if __name__ == '__main__':
    __main__()

'''
tello information

25 mm focal length

82.6 fov

2592 x 1936 res

'''


#def main():
    #rospy.init_node('driver', anonymous=True)
    #tello = Tello()
    #tello.connect(False)
    #"""pub_state = rospy.Publisher('/tello/state', State, queue_size = 10)"""
    #rospy.Subscriber("/tello/flip", Flip, callback_flip)
    #rospy.Subscriber("/tello/cmd_vel", Twist, callback_cmd_vel)
    #rospy.Subscriber("/tello/takeoff", Empty, callback_flip)
    #rospy.Subscriber("/tello/land", Empty, callback_flip)
    #pub_camera = 

"""
def callback_flip(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)

def callback_cmd_vel(msg):
    te
    




def flip_sub():
    
    rospy.init_node('flip_sub', anonymous=True)
    rospy.Subscriber("flip", String, callback_flip)
    rospy.spin()









"""
"""
def callback_velocity()

def camera_pub():
    pub = rospy.Publisher('camera', )
    rospy.init_node('driver', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

    """


"""def camera_pub():



def state_pub():
pub = rospy.Publisher('state',)
rospy.init_node('driver', anonymous=True)
rate = rospy.Rate(10)
while not rospy.is_shutdown():

battery
flighttime

vector3

from package import message"""    



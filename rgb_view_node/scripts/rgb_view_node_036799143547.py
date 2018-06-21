#!/usr/bin/env python

# Python libs
import sys
import time
import threading
import subprocess

# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2
from cv_bridge import CvBridge, CvBridgeError

# Ros libraries
import roslib
import rospy
import rosbag

# Ros Messages
from sensor_msgs.msg import Image

DEVICE_SERIAL = "036799143547"


# We do not use cv_bridge it does not support CompressedImage in python
# from cv_bridge import CvBridge, CvBridgeError

class RGB_subscriber:

    def __init__(self):
        self.frames = 0
        self.bag = rosbag.Bag('rgb.bag', 'w')
        self.bridge = CvBridge()

    def callback(self, msg):
        try:
            # Convert your ROS Image message to OpenCV2
                        
            self.bag.write('rgb', msg)

            self.frames += 1
            rospy.loginfo('frame: '+ str(self.frames))

        except CvBridgeError, e:
            print(e)
        
        #cv2.imwrite('/home/inderjeet/images/camera_image.jpeg', cv2_img)
        """
        if self.frames > 100:
            print('reached frame limit')
            #rospy.signal_shutdown("Reached frame limit.")
            self.rgb_sub.unregister()
            self.read_img()
        """

    def read_img(self):

        try: 
            bag = rosbag.Bag('rgb.bag')
            bag.reindex()
            for msg in bag.read_messages(topics=['rgb']):
                cv2_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                cv2.imshow('hi', cv2_img)
            bag.close()
        except Exception as e:
            print 'Error in read_img(): ' + str(e)
            
        player_proc = subprocess.Popen(['rosbag', 'play', 'rgb.bag'], '/home/inderjeet/catkin_ws/rgb.bag')

    def main(self):
        rospy.init_node("rgb_view" + DEVICE_SERIAL)
        self.rgb_sub = rospy.Subscriber("/kinect2_" + DEVICE_SERIAL + "/sd/image_color_rect",
                         Image, self.callback)

        rospy.spin()


if __name__ == "__main__":
    run = RGB_subscriber()
    run.main()

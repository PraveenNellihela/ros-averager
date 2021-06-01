#!usr/bin/env python3

import rospy
from std_msgs.msg import Float32

from scipy import signal
import numpy as np


def square_generator():                                     # to do - add freq, amp etc here as params
    rospy.init_node('square_generator')
    pub = rospy.Publisher('~raw', Float32, queue_size=10)
    rate = rospy.Rate(10)
    resolution = 10

    t = np.linspace(0, rospy.get_param("/signal_length"), resolution*rospy.get_param("/signal_length"))
    square = rospy.get_param("/amplitude")*signal.square(2*np.pi*rospy.get_param("/frequency")*t) + rospy.get_param("/offset")

    while not rospy.is_shutdown():
        for val in square:
            publish_val = val
            rospy.loginfo(publish_val)
            pub.publish(publish_val)
            rate.sleep()


if __name__ == '__main__':
    square_generator()

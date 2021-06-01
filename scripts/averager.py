#!usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import statistics

n = rospy.get_param("/buffer_size")
total = []

pub = rospy.Publisher('avg', Float32, queue_size=10)
def calculate_avg(data):
    for i in range(n):
        total.append(data.data)
    pub.publish(statistics.mean(total))


def averager():
    rospy.init_node('averager')
    rospy.Subscriber('~raw', Float32, calculate_avg)
    rospy.spin()

if __name__ == '__main__':
    averager()

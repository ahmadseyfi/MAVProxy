#!/usr/bin/python
# Filename: sync_ros.py
import rospy

def time():
	val = rospy.get_time() + 1420070400
	#print "val = ", val
	return val

def sleep(x):
	#print 'Bye, this was the module'
	rospy.sleep(x)

version = '0.1'

# End of mymodule.py

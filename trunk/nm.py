import sys, os, string
import time


class record:
	def __init__(self):
		self.x=0
		self.y=0
y = record()
y.z = 2
print y.__dict__
print dir(y)

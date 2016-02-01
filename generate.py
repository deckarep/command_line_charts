#!/usr/bin/env python
 
import time
from sys import stdout
import random

while True:                                     
	time.sleep(0.5)
	# dogs
	x = random.randint(1,10)
	print "{},{}".format("cats", x)

	# cats
	x = random.randint(1,10)
	print "{},{}".format("dogs", x)

	stdout.flush()


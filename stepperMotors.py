#The purpose of this function is to run a stepper motor
#Using a A4988 stepper motor driver
#Program expects two arguments: direction and steps
#Usage: sudo python stepper.py left 1600

#Import libraries
	import sys
	import RPi.GPIO as gpio
	import time 	

#Read arguments
	try:
		direction = sys.argv[1]
		steps = int(float(sys.argv[2]))
	except:
		steps = 0

	print("Turning %s %s steps") % (direction, steps)

#RPi GPIO 
	gpio.setmode(gpio.BCM)
	#GPIO23 = direction
	#GPIO24 = step
	gpio.setup(23,gpio.OUT)
	gpio.setup(24,gpio.OUT)

#Direction
	#output is true to the left and false to the right
	if direction = 'left':
		gpio.output(23, true)
	elif direction == 'right':
		gpio.output(23, false)

#Step counter and speed control
	stepCounter = 0
	waitTime = 0.000001
	
#Implement
	while stepCounter < steps:
		#GPIO on/off signals one step
		gpio.output(24, true)
		gpio.output(24, false)
		stepCounter += 1
		#control rotation speed
		time.sleep(waitTime) 

#Reset GPIO
			gpio.cleanup()
			
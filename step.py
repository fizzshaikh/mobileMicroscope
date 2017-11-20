#Import libraries
import sys
import time
from time import sleep
import RPi.GPIO as GPIO

#Set pins and directions
dir = 20
step = 21
cw = 1 #clockwise rotation
ccw = 0 #counterclockwise
spr = 0 #steps per revolution (360/7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dir, GPIO.OUT)
GPIO.setup(step, GPIO.OUT)
GPIO.output(dir, cw)

step_count = spr
delay = 0.0208

#Normal steps
for x in range(step_count):
	GPIO.output(step, GPIO.HIGH)
	sleep(delay)
	GPIO.output(step, GPIO.LOW)
	sleep(delay)

sleep(0.5)
GPIO.output(dir, ccw)

for x in range(step_count):
	GPIO.output(step, GPIO.HIGH)
	sleep(delay)
	GPIO.output(step, GPIO.LOW)
	sleep(delay)

#Microstepping
MODE = (14,15,18)
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full':(0,0,0),
	'Half':(1,0,0),
	'1/4':(0,1,0),
	'1/8':(1,1,0)
	'1/16':(0,0,1)
	'1/32':(1,0,1)}
GPIO.output(MODE, RESOLUTION['1/32'])

step_count=spr*32
delay=0.0208/32

GPIO.cleanup()

#backup code from another source
#https://www.raspberrypi.org/forums/viewtopic.php?t=110368

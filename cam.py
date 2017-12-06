#Make sure that the camera is enabled
#Install library with sudo apt-get update and sudo apt-get install python3-picamera

import picamera
camera = picamera.PiCamera()
camera.capture('image.jpg')

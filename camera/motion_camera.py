# GD 17/02/2023
#
# Simple script for interfacing with 2 things:
#   - PIR motion sensor
#   - Pi Zero Camera
#
# Ensure to enable the camera module first (sudo raspi-config)
# Essentially a basic security camera setup that records a video for 10 seconds everytime motion is detected.
# Video names are timestamped

from gpiozero import MotionSensor
from picamera import PiCamera
import time
import datetime

def timeStamp(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 90

while True:
    pir.wait_for_motion()
    camera.start_recording('/home/pi/cam/vid/' + timeStamp('video.h264'))
    time.sleep(10)
    camera.stop_recording()
    pir.wait_for_no_motion()
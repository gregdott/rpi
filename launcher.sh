#!/bin/sh
# launcher.sh
# Just a template for what is needed to run script on startup on rpi
# 
# sudo crontab -e
# add the following line
# @reboot sh /home/pi/path-to-this-script/launcher.sh >/home/pi/path-to-log-file 2>&1

sudo python3 /home/pi/path-to-script/script.py
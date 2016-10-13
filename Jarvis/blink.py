#! /usr/bin/env python
# this script is just to test stuff. You should probably ignore this.
import RPi.GPIO
import time

gpio = RPi.GPIO

gpio.setmode(gpio.BCM) # So I can refer to each pin by it's GPIO number
gpio.setup(2, gpio.OUT)

i = 0

while i < 10:
	gpio.output(2, True) #or gpio.HIGH and gpio.LOW
	time.sleep(0.3)
	gpio.output(2, False)
	time.sleep(0.3)
	i += 1 # one cycle is on and off
gpio.cleanup()

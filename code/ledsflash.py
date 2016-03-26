#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define LEDs
led_6 = 8
led_5 = 10
led_4 = 12
led_3 = 16
led_2 = 18
led_1 = 22

leds = (8, 10, 12, 16, 18, 22)

# Setup LEDs
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(led_4, GPIO.OUT)
GPIO.setup(led_5, GPIO.OUT)
GPIO.setup(led_6, GPIO.OUT)

# Testing LEDs
for x in leds:
    GPIO.output(x, 1)
    time.sleep(0.05)
    GPIO.output(x, 0)

for x in reversed(leds):
    GPIO.output(x, 1)
    time.sleep(0.05)
    GPIO.output(x, 0)


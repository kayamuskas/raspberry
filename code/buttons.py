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

# Define buttons
button_6 = 3
button_5 = 5
button_4 = 7
button_3 = 11
button_2 = 13
button_1 = 15

# Setup buttons
GPIO.setup(button_1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_4, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_5, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_6, GPIO.IN, GPIO.PUD_UP)

# Testing buttons
while True:
    if GPIO.input(button_1) == False:
            print("1 button pressed")
	    GPIO.output(led_1, 1)
	    time.sleep(0.2)
	    GPIO.output(led_1, 0)
	    time.sleep(0.1)
    if GPIO.input(button_2) == False:
            print("2 button pressed")
	    GPIO.output(led_2, 1)
	    time.sleep(0.2)
	    GPIO.output(led_2, 0)
	    time.sleep(0.1)
    if GPIO.input(button_3) == False:
            print("3 button pressed")
	    GPIO.output(led_3, 1)
	    time.sleep(0.2)
	    GPIO.output(led_3, 0)
	    time.sleep(0.1)
    if GPIO.input(button_4) == False:
            print("4 button pressed")
	    GPIO.output(led_4, 1)
	    time.sleep(0.2)
	    GPIO.output(led_4, 0)
	    time.sleep(0.1)
    if GPIO.input(button_5) == False:
            print("5 button pressed")
	    GPIO.output(led_5, 1)
	    time.sleep(0.2)
	    GPIO.output(led_5, 0)
	    time.sleep(0.1)
    if GPIO.input(button_6) == False:
            print("6 button pressed")
	    GPIO.output(led_6, 1)
	    time.sleep(0.2)
	    GPIO.output(led_6, 0)
	    time.sleep(0.1)

# Clear all
GPIO.cleanup()

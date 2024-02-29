#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

led = 7
button = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

try:
    while True:
        i = GPIO.input(button)
        if i == 0:
            GPIO.output(led, GPIO.HIGH)
        else:
            GPIO.output(led,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done")

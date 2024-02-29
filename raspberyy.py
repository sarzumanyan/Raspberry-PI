#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

led = 14 
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        GPIO.output(led, GPIO.HIGH)
        print("led is on")
        time.sleep(2)

        GPIO.output(led,GPIO.LOW)
        print("led is off")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

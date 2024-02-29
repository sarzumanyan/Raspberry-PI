#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

led = 7
button = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
count = 0
try:
    while True:
        i = GPIO.input(button)
        if i == 0 and count%2 == 1:
            GPIO.output(led, GPIO.HIGH)
        elif i==1 and count % 2 == 0:
            GPIO.output(led,GPIO.LOW)
        count+=1
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done")

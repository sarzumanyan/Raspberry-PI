#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

led = 7
button = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN,pull_up_down=GPIO.PUD_UP)
try:
    while True:
        if GPIO.input(button) == GPIO.LOW:
            GPIO.output(led,not GPIO.input(led))
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done")

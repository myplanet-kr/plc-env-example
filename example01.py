import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pirPin = 7

GPIO.setup(pirPin, GPIO.IN)

latest = 0
while True:
    current = GPIO.input(pirPin)
    if current == 0 & current != latest:
        print("data push")
    latest = current
    time.sleep(0.2)
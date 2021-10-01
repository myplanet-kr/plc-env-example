import RPi.GPIO as GPIO
import time
import requests

pirPin = 7
GPIO.setmode(GPIO.BCM)

GPIO.setup(pirPin, GPIO.IN)
latest = 0

# request config
URL = 'http://localhost:8000'
path = '/device/auto'
headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'xxxxxxxxxxxxxxxxxxxxxxxx'}
data = {qty: 1, inferiorQty: 0, produceLineId: 1}

while True:
    current = GPIO.input(pirPin)
    if current == 0 & current != latest:
        res = requests.post(URL, headers=headers, data=data)
        print("data push")
    latest = current
    time.sleep(0.2)
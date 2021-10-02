import RPi.GPIO as GPIO
import time
import requests
import time
import os

print('# PLC Environment Activation')
i = 0
dots = 'now loading.'
while i <= 3:
    time.sleep(1)
    if (i == 0):
        os.system('clear')
    print(dots)
    i += 1
    dots += '..'
time.sleep(1)
os.system('clear')

print('-----------------------------------')
print('0. 도메인 주소를 입력해주세요.')
addr = input()

print('1. device 토큰을 입력해주세요.')
token = input()

print('2. 생산 라인번호를 입력해주세요.')
produceLineId = input()

print('3-1. 생산 수량을 입력해주세요.')
qty = input()
print('3-2. 불량 수량을 입력해주세요.')
inferiorQty = input()
pirPin = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)
latest = 0

# request config
path = '/device/auto'
URL = addr + path
headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer ' + token}
data = {'qty': qty, 'inferiorQty': inferiorQty, 'produceLineId': produceLineId}

while True:
    current = GPIO.input(pirPin)
    if current == 0 & current != latest:
        res = requests.get(URL, headers=headers, data=data)
    latest = current
    time.sleep(0.2)

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
print('0. 도메인 주소를 입력해주세요. (기본:https://api.dotoritory.com) ')
addr = input()
if (addr == ''): addr = 'https://api.dotoritory.com'
print('1. device 토큰을 입력해주세요.')
token = input()
if (token == ''):
    raise ValueError('token값은 필수적으로 입력돼야 합니다.')

print('2. 생산 라인번호를 입력해주세요. (기본: 0)')
produceLineId = input()
print('3-1. 생산 수량을 입력해주세요. (기본: 1)')
qty = input()
if (qty == ''): qty = 1
print('3-2. 불량 수량을 입력해주세요. (기본: 0)')
inferiorQty = input()
if (inferiorQty == ''): inferiorQty = 0
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
        print('censored')
        res = requests.get(URL, headers=headers, data=data)
        print(res)
    latest = current
    time.sleep(0.2)

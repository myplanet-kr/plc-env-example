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
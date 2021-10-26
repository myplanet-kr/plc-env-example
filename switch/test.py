# -*- coding: utf-8 -*-

import os
import sys
import time

import RPi.GPIO as GPIO

from line import line
from ment import init_script, set_line_config_script
from server import set_dotori_server_config_script

sys.dont_write_bytecode = True
GPIO.setmode(GPIO.BCM)
BCM_LIST = [14, 23, 24]
LINE_LIST = []

init_script()
dotori_server = set_dotori_server_config_script()

i = 0
while i < len(BCM_LIST):
    if i != 0:
        res = input('생산 라인 추가를 중지하려면 0, 추가 하시려면 아무키나 눌러주세요.')
        if res == '0':
            break
    genLine = line(BCM_LIST[i], len(LINE_LIST))
    filledGenLine = set_line_config_script(genLine)
    LINE_LIST.append(filledGenLine)
    i += 1
os.system('clear')

print('생산 라인 설정 완료')

for l in LINE_LIST:
    l.self_introduce()
    cb = l.make_callback(dotori_server)
    l.io_initialize(cb)
try:
    while 1:
        print(".")
        time.sleep(0.1)
finally:
    GPIO.cleanup()
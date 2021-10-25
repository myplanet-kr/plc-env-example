# -*- coding: utf-8 -*-
import os
import time
from server import server
from line import line

def init_script():
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

def set_line_config_script(l):
  produceLineId = input('2. 생산 라인번호를 입력해주세요. (기본: 0)')
  if (produceLineId == ''): produceLineId = '0'
  qty = input('3-1. 생산 수량을 입력해주세요. (기본: 1)')
  if (qty == ''): qty = '1'
  inferiorQty = input('3-2. 불량 수량을 입력해주세요. (기본: 0)')
  if (inferiorQty == ''): inferiorQty = '0'
  l.add_info(int(produceLineId), int(qty), int(inferiorQty))
  return l
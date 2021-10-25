# -*- coding: utf-8 -*-
import requests
import RPi.GPIO as GPIO

from request_handler import get_request


class line:
    def __init__(self, BCM, seq):
        self.BCM = BCM
        self.name = seq + 1
        self.id = 0
        self.qty = 0
        self.errorQty = 0

    def add_info(self, id, qty, errorQty):
        self.id = id
        self.qty = qty
        self.errorQty = errorQty

    def self_introduce(self):
        print('-----------------------------')
        print('[%d번 생산 라인]'%self.name)
        print('produce-line-id: %d'%self.id)
        print('생산량: %d'%self.qty)
        print('불량수량: %d'%self.errorQty)
        print('-----------------------------')
    
    def make_callback(self, server):
        [URL, headers, data] = get_request(server, self)
        def get_func():
            print('%s line called'%self.name)
            r = requests.get(URL, headers=headers, data=data)
            print(r.content)
        return get_func
            

    def io_initialize(self, callback):
        GPIO.setup(self.BCM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.BCM, GPIO.RISING, callback, bouncetime=200)
    
import RPi.GPIO as GPIO
import time

# 스위치 눌렸을 때 콜백함수
def switchPressed(channel):
        print('channel %s pressed!!'%channel)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# interrupt 선언
GPIO.add_event_detect(24, GPIO.RISING, callback=switchPressed, bouncetime=200)
# 메인 쓰레드
try:
    while 1:
        print(".")
        time.sleep(0.1)
finally:
    GPIO.cleanup()
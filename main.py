import time

import RPi.GPIO as GPIO
import getch


# PIN_NUM = [2, 3, 4, 17, 27, 22, 10]
PIN_NUM = [2, 3, 4]

DEL_TIME = 0.1

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    for n in PIN_NUM:
        GPIO.setup(n, GPIO.OUT)

def bang(pin):
    GPIO.output(pin, 1)
    time.sleep(0.01)
    GPIO.output(pin, 0)
    time.sleep(DEL_TIME - 0.01)

def serial(key):
    print('{}: {:07b}'.format(key.encode('utf-8'), ord(key)))
    b = int(ord(key))

    # start bang
    bang(PIN_NUM[0])

    # send 1 byte
    for i in range(8):
        if (b >> i) & 0b1:
            bang(PIN_NUM[0])

def parallel(key):
    # 8bit以下だけ通すようにしたい
    print('{}: {:07b}'.format(key.encode('utf-8'), ord(key)))
    b = int(ord(key))

    for i, pin in enumerate(PIN_NUM):
        if (b >> i) & 0b1:
            GPIO.output(pin, 1)
    
    time.sleep(0.01)

    for pin in PIN_NUM:
        GPIO.output(pin, 0)

def main():
    # input()を利用
            print('please enter characters')
            keys = input()
            for key in keys:
                parallel(key)
                time.sleep(0.1)

def main2():
    # 押したキーにすぐ反応ver
        key = getch.getch()
        serial(key)

if __name__ == '__main__':
    setupGPIO()
    try:
        while True:
            main2()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('end')

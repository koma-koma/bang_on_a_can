import time

import RPi.GPIO as GPIO
import getch


# PIN_NUM = [2, 3, 4, 17, 27, 22, 10]
PIN_NUM = [2, 3, 4]


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    for n in PIN_NUM:
        GPIO.setup(n, GPIO.OUT)


def interpretation(key):
    print('{}: {:07b}'.format(key.encode('utf-8'), ord(key)))
    b = int(ord(key))

    for i, pin in enumerate(PIN_NUM):
        if (b >> i) & 0b1:
            GPIO.output(pin, 1)
    
    time.sleep(0.01)

    for pin in PIN_NUM:
        GPIO.output(pin, 0)


if __name__ == '__main__':
    setupGPIO()
    try:
        while True:
            key = getch.getch()
            # 8bit以下だけ通すようにする
            interpretation(key)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('end')

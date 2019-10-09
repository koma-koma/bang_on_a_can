import RPi.GPIO as GPIO
import getch


PIN_NUM = [2, 3, 4]

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    for n in PIN_NUM:
        GPIO.setup(n,GPIO.OUT)


def interpretation(key):
    print('{}: {:07b}'.format(key.encode('utf-8'), ord(key)))


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
            

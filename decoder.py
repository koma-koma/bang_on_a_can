import time

import RPi.GPIO as GPIO


PIN_NUM = [2, 3]

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    for n in PIN_NUM:
        GPIO.setup(n, GPIO.IN)

def detect_ascii():

    
    char = 
    return char

def main():
    for pin in PIN_NUM:
        print(GPIO.input(pin), end=" ")
    print('')
    time.sleep(1)

if __name__ == '__main__':
    setupGPIO()
    try:
        while True:
            main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('end')
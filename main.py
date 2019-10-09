import RPi.GPIO as GPIO
import getch


def setupGPIO():
    pass


def interpretation(key):
    print('{}: {:07b}'.format(key.encode('utf-8'), ord(key)))


if __name__ == '__main__':
    while True:
        try:
            key = getch.getch()
            interpretation(key)
        except:
            pass
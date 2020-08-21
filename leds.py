import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(21, GPIO.IN, GPIO.PUD_UP)
while True:
    if not GPIO.input(21):
        GPIO.output(23, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(25, GPIO.LOW)
import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
GPIO.setwarnings(False)
TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
while True:
    GPIO.output(TRIG, True)                    #Set TRIG as HIGH
    time.sleep(2)
    GPIO.output(TRIG, False)
    time.sleep(2)

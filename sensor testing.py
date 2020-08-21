import RPi.GPIO as GPIO
from sense_emu import SenseHat
sense = SenseHat()
import time
from time import sleep
from gpiozero import LightSensor, Buzzer
import sys

#GPIO startup settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Buzzer config
buzzer = 18
GPIO.setup(buzzer, GPIO.OUT)
buzz = GPIO.PWM(buzzer, 440)
#LDR config
LDR = LightSensor(21)
#Ultrasonic Config
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#################################################################################
#ULTRASONIC TESTING#
#################################################################################



#################################################################################
#BUZZER TESTING#
#################################################################################
C3 = 130.813
Csharp3 = 138.591
D3 = 146.832
Dsharp3 = 155.563
E3 = 164.814
F3 = 174.614
Fsharp3 = 184.997
G3 = 195.998
Gsharp3 = 207.652
A3 = 220
Asharp3 = 233.082
B3 = 246.942
C4 = 277.183
Csharp4 = 277.183
D4 = 293.665
Dsharp4 = 311.127
E4 = 329.628
F4 = 349.228
Fsharp4 = 369.994
G4 = 391.995
Gsharp4 = 415.305
A4 = 440
Asharp4 = 466.164
B4 = 493.883
C5 = 523.251
Csharp5 = 554.365
D5 = 587.330
Dsharp5 = 622.254
E5 = 659.255
F5 = 698.456
Fsharp5 = 739.989
G5 = 783.991
Gsharp5 = 830.609
A5 = 880
Asharp5 = 932.328
B5 = 985.767
C6 = 1046.50

buzz.start(50)
buzz.ChangeFrequency(C6)
sleep(0.1)
buzz.ChangeFrequency(B5)
sleep(0.1)
buzz.ChangeFrequency(A5)
sleep(0.1)
buzz.ChangeFrequency(G5)
sleep(0.1)
buzz.ChangeFrequency(F5)
sleep(0.1)
buzz.ChangeFrequency(E5)
sleep(0.1)
buzz.ChangeFrequency(D5)
sleep(0.1)
buzz.ChangeFrequency(C5)
sleep(0.1)
buzz.ChangeFrequency(B4)
sleep(0.1)
buzz.ChangeFrequency(A4)
sleep(0.1)
buzz.ChangeFrequency(G4)
sleep(0.1)
buzz.ChangeFrequency(F4)
sleep(0.1)
buzz.ChangeFrequency(E4)
sleep(0.1)
buzz.ChangeFrequency(D4)
sleep(0.1)
buzz.ChangeFrequency(C4)
sleep(0.1)
buzz.ChangeFrequency(B3)
sleep(0.1)
buzz.ChangeFrequency(A3)
sleep(0.1)
buzz.ChangeFrequency(G3)
sleep(0.1)
buzz.ChangeFrequency(F3)
sleep(0.1)
buzz.ChangeFrequency(E3)
sleep(0.1)
buzz.ChangeFrequency(D3)
sleep(0.1)
buzz.ChangeFrequency(C3)
sleep(0.1)
buzz.stop()




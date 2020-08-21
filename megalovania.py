#Megalovania On the Pi with a Buzzer
#By Matthew Tong
#Put buzzer on GPIO pin 21

import RPi.GPIO as GPIO
import sys
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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
GPIO.setup(18, GPIO.OUT)


buzz = GPIO.PWM(18, 440)
buzz.start(50)
buzz.ChangeFrequency(D4)
sleep(0.125)
buzz.ChangeFrequency(D4)
sleep(0.125)
buzz.ChangeFrequency(D5)
sleep(0.3)
buzz.ChangeFrequency(A4)
sleep(0.3)
buzz.ChangeFrequency(Gsharp4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(D4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(C4)
sleep(0.125)
buzz.ChangeFrequency(C4)
sleep(0.125)
buzz.ChangeFrequency(D5)
sleep(0.3)
buzz.ChangeFrequency(A4)
sleep(0.3)
buzz.ChangeFrequency(Gsharp4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(D4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(B3)
sleep(0.125)
buzz.ChangeFrequency(B3)
sleep(0.125)
buzz.ChangeFrequency(D5)
sleep(0.3)
buzz.ChangeFrequency(A4)
sleep(0.3)
buzz.ChangeFrequency(Gsharp4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(D4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(Asharp3)
sleep(0.125)
buzz.ChangeFrequency(Asharp3)
sleep(0.125)
buzz.ChangeFrequency(D5)
sleep(0.3)
buzz.ChangeFrequency(A4)
sleep(0.3)
buzz.ChangeFrequency(Gsharp4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(D4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(D4)
sleep(0.125)
buzz.ChangeFrequency(D4)
sleep(0.125)
buzz.ChangeFrequency(D5)
sleep(0.3)
buzz.ChangeFrequency(A4)
sleep(0.3)
buzz.ChangeFrequency(Gsharp4)
sleep(0.190)
buzz.ChangeFrequency(G4)
sleep(0.190)
buzz.ChangeFrequency(F4)
sleep(0.190)
buzz.ChangeFrequency(D4)
sleep(0.190)

sys.exit()
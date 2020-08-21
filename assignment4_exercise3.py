import RPi.GPIO as GPIO
import sys
from gpiozero import Button
from time import sleep
from gpiozero import LightSensor, Buzzer
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
global buzz
ledA = 18
ledB = 12
buttonY = 15
buttonZ = Button(7)
ldr = LightSensor(4)
buzzer = 21
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
GPIO.setup(21, GPIO.OUT)
GPIO.setup(ledA, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(buttonY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
buzz = GPIO.PWM(buzzer, 440)
buzz.start(0)
def button_callback():
    sys.exit()

def play_frequencies(list_frequencies, number_iteration):
    for i in list_frequencies:
        for j in range(0, int(number_iteration)):
            if i > 200 and i < 10000 and ldr.value > 0:
                buzz.ChangeFrequency(i)
                sleep(0.1)
                GPIO.output(ledA, GPIO.HIGH)
                print("Buzz")
                sleep(0.5)
                GPIO.output(ledA, GPIO.LOW)
                GPIO.add_event_detect(buttonY, GPIO.RISING,callback=button_callback)
            
            elif ldr.value < 0:
                while True:
                    print("Shine a light")
            
            elif i < 200 or i > 10000:
                sleep(0.1)
                GPIO.output(ledB, GPIO.HIGH)
                print("No buzz")
                sleep(0.5)
                GPIO.output(ledB, GPIO.LOW)
                sleep(0.5)
            
buttonZ.wait_for_press()
play_frequencies((100, 200, 300, 400, 500), 3)



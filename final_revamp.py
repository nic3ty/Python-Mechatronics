import RPi.GPIO as GPIO
import sys
import time
from gpiozero import LightSensor
from sense_hat import SenseHat
print(sys.getrecursionlimit())
#from picamera import PiCamera
#camera = PiCamera()
sense = SenseHat()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Pins for different peripherals
LDR = LightSensor(24)
buzzer = 6
interrupt = 13
GPIO.setup(buzzer, GPIO.OUT)
buzz = GPIO.PWM(buzzer, 440)
TRIG = 18
ECHO = 17
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(interrupt, GPIO.OUT)

#Distances at which the risk/danger levels are
#Another threshold could be speed: if speed > Threshold and distance < HazardThresholdNear stop all operations
HazardThresholdNear = 15.00
HazardThresholdMid = 20.00
HazardThresholdFar = 30.00
#SenseHat pixel calibration
sense.load_image("sense-hat-graphics2.jpg")
sense.clear()
one_row = [255, 0 ,42]
two_row = [255, 72, 0]
three_row = [255, 94, 0]
four_five_six_row = [255, 127, 0]
seven_row = [255, 166, 0]
eight_row = [255, 195, 0]
blank = [0, 0, 0]
def distance_sample():
    GPIO.output(interrupt, GPIO.HIGH)
    time.sleep(0.025)
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    time.sleep(.1)                            #Delay of 2 seconds
    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_star = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_star #Get pulse duration to a variable

    distance2 = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance2 = round(distance2, 2)            #Round to two decimal points
    return distance2
def sense_hat_ledNear():
    sense.set_pixel(7, 7, one_row)
    sense.set_pixel(7, 6, one_row)
    sense.set_pixel(7, 5, one_row)
    sense.set_pixel(7, 4, one_row)
    sense.set_pixel(7, 3, one_row)
    sense.set_pixel(7, 2, one_row)
    sense.set_pixel(7, 1, one_row)
    sense.set_pixel(6, 7, two_row)
    sense.set_pixel(6, 6, two_row)
    sense.set_pixel(6, 5, two_row)
    sense.set_pixel(6, 4, two_row)
    sense.set_pixel(6, 3, two_row)
    sense.set_pixel(6, 2, two_row)
    sense.set_pixel(6, 1, two_row)
    sense.set_pixel(5, 7, three_row)
    sense.set_pixel(5, 6, three_row)
    sense.set_pixel(5, 5, three_row)
    sense.set_pixel(5, 4, three_row)
    sense.set_pixel(5, 3, three_row)
    sense.set_pixel(5, 2, three_row)
    sense.set_pixel(5, 1, three_row)
    sense.set_pixel(4, 7, four_five_six_row)
    sense.set_pixel(4, 6, four_five_six_row)
    sense.set_pixel(4, 5, four_five_six_row)
    sense.set_pixel(4, 4, four_five_six_row)
    sense.set_pixel(4, 3, four_five_six_row)
    sense.set_pixel(4, 2, four_five_six_row)
    sense.set_pixel(4, 1, four_five_six_row)
    sense.set_pixel(3, 7, four_five_six_row)
    sense.set_pixel(3, 6, four_five_six_row)
    sense.set_pixel(3, 5, four_five_six_row)
    sense.set_pixel(3, 4, four_five_six_row)
    sense.set_pixel(3, 3, four_five_six_row)
    sense.set_pixel(3, 2, four_five_six_row)
    sense.set_pixel(3, 1, four_five_six_row)
    sense.set_pixel(2, 7, four_five_six_row)
    sense.set_pixel(2, 6, four_five_six_row)
    sense.set_pixel(2, 5, four_five_six_row)
    sense.set_pixel(2, 4, four_five_six_row)
    sense.set_pixel(2, 3, four_five_six_row)
    sense.set_pixel(2, 2, four_five_six_row)
    sense.set_pixel(2, 1, four_five_six_row)
    sense.set_pixel(1, 7, seven_row)
    sense.set_pixel(1, 6, seven_row)
    sense.set_pixel(1, 5, seven_row)
    sense.set_pixel(1, 4, seven_row)
    sense.set_pixel(1, 3, seven_row)
    sense.set_pixel(1, 2, seven_row)
    sense.set_pixel(1, 1, seven_row)
    sense.set_pixel(0, 7, eight_row)
    sense.set_pixel(0, 6, eight_row)
    sense.set_pixel(0, 5, eight_row)
    sense.set_pixel(0, 4, eight_row)
    sense.set_pixel(0, 3, eight_row)
    sense.set_pixel(0, 2, eight_row)
    sense.set_pixel(0, 1, eight_row)

def sense_hat_ledFarther():
    sense.set_pixel(7, 7, blank)
    sense.set_pixel(7, 6, blank)
    sense.set_pixel(7, 5, blank)
    sense.set_pixel(7, 4, blank)
    sense.set_pixel(7, 3, blank)
    sense.set_pixel(7, 2, blank)
    sense.set_pixel(7, 1, blank)
    sense.set_pixel(6, 7, blank)
    sense.set_pixel(6, 6, blank)
    sense.set_pixel(6, 5, blank)
    sense.set_pixel(6, 4, blank)
    sense.set_pixel(6, 3, blank)
    sense.set_pixel(6, 2, blank)
    sense.set_pixel(6, 1, blank)
    sense.set_pixel(5, 7, blank)
    sense.set_pixel(5, 6, blank)
    sense.set_pixel(5, 5, blank)
    sense.set_pixel(5, 4, blank)
    sense.set_pixel(5, 3, blank)
    sense.set_pixel(5, 2, blank)
    sense.set_pixel(5, 1, blank)
    sense.set_pixel(4, 7, blank)
    sense.set_pixel(4, 6, blank)
    sense.set_pixel(4, 5, blank)
    sense.set_pixel(4, 4, blank)
    sense.set_pixel(4, 3, blank)
    sense.set_pixel(4, 2, blank)
    sense.set_pixel(4, 1, blank)
    sense.set_pixel(3, 7, blank)
    sense.set_pixel(3, 6, blank)
    sense.set_pixel(3, 5, blank)
    sense.set_pixel(3, 4, blank)
    sense.set_pixel(3, 3, blank)
    sense.set_pixel(3, 2, blank)
    sense.set_pixel(3, 1, blank)
    sense.set_pixel(2, 7, blank)
    sense.set_pixel(2, 6, blank)
    sense.set_pixel(2, 5, blank)
    sense.set_pixel(2, 4, blank)
    sense.set_pixel(2, 3, blank)
    sense.set_pixel(2, 2, blank)
    sense.set_pixel(2, 1, blank)
    sense.set_pixel(1, 7, blank)
    sense.set_pixel(1, 6, blank)
    sense.set_pixel(1, 5, blank)
    sense.set_pixel(1, 4, blank)
    sense.set_pixel(1, 3, blank)
    sense.set_pixel(1, 2, blank)
    sense.set_pixel(1, 1, blank)
    sense.set_pixel(0, 7, blank)
    sense.set_pixel(0, 6, blank)
    sense.set_pixel(0, 5, blank)
    sense.set_pixel(0, 4, blank)
    sense.set_pixel(0, 3, blank)
    sense.set_pixel(0, 2, blank)
    sense.set_pixel(0, 1, blank)
Fault = False
GPIO.output(interrupt, GPIO.HIGH)
while True:
    GPIO.output(interrupt, GPIO.HIGH)
    time.sleep(0.025)
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    time.sleep(0.025)                            #Delay of 2 seconds
    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_star = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_star #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points
    accel = sense.get_accelerometer_raw()
    x = accel['x']
    
    if Fault == True:
        sense_hat_ledNear()
        buzz.start(50)
        buzz.ChangeFrequency(554.37)
        #camera.capture('/home/pi/Downloads/danger.jpg')
        GPIO.output(interrupt, GPIO.LOW)
        print("Before button")
        while Fault == True:
            print("While fault = true")
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    Fault = False
                    print("Pressed")
                    print("Fault = False")
                    sense.clear()
                    buzz.stop()
                else:
                    Fault = True
                    print("Fault = True")
    elif Fault == False:
        print("Fault = False")
        GPIO.output(interrupt, GPIO.HIGH)
        distance2 = distance_sample()
        if distance2 < HazardThresholdNear:
            Fault = True
            print("Tripped")
        else:
            Fault = False
        
        if distance2 < HazardThresholdMid:
            sense.set_pixel(4, 7, four_five_six_row)
            sense.set_pixel(4, 6, four_five_six_row)
            sense.set_pixel(4, 5, four_five_six_row)
            sense.set_pixel(4, 4, four_five_six_row)
            sense.set_pixel(4, 3, four_five_six_row)
            sense.set_pixel(4, 2, four_five_six_row)
            sense.set_pixel(4, 1, four_five_six_row)
            sense.set_pixel(3, 7, four_five_six_row)
            sense.set_pixel(3, 6, four_five_six_row)
            sense.set_pixel(3, 5, four_five_six_row)
            sense.set_pixel(3, 4, four_five_six_row)
            sense.set_pixel(3, 3, four_five_six_row)
            sense.set_pixel(3, 2, four_five_six_row)
            sense.set_pixel(3, 1, four_five_six_row)
            sense.set_pixel(2, 7, four_five_six_row)
            sense.set_pixel(2, 6, four_five_six_row)
            sense.set_pixel(2, 5, four_five_six_row)
            sense.set_pixel(2, 4, four_five_six_row)
            sense.set_pixel(2, 3, four_five_six_row)
            sense.set_pixel(2, 2, four_five_six_row)
            sense.set_pixel(2, 1, four_five_six_row)
            sense.set_pixel(1, 7, seven_row)
            sense.set_pixel(1, 6, seven_row)
            sense.set_pixel(1, 5, seven_row)
            sense.set_pixel(1, 4, seven_row)
            sense.set_pixel(1, 3, seven_row)
            sense.set_pixel(1, 2, seven_row)
            sense.set_pixel(1, 1, seven_row)
            sense.set_pixel(0, 7, eight_row)
            sense.set_pixel(0, 6, eight_row)
            sense.set_pixel(0, 5, eight_row)
            sense.set_pixel(0, 4, eight_row)
            sense.set_pixel(0, 3, eight_row)
            sense.set_pixel(0, 2, eight_row)
            sense.set_pixel(0, 1, eight_row)
        elif distance2 < HazardThresholdFar:
            sense.set_pixel(1, 7, seven_row)
            sense.set_pixel(1, 6, seven_row)
            sense.set_pixel(1, 5, seven_row)
            sense.set_pixel(1, 4, seven_row)
            sense.set_pixel(1, 3, seven_row)
            sense.set_pixel(1, 2, seven_row)
            sense.set_pixel(1, 1, seven_row)
            sense.set_pixel(0, 7, eight_row)
            sense.set_pixel(0, 6, eight_row)
            sense.set_pixel(0, 5, eight_row)
            sense.set_pixel(0, 4, eight_row)
            sense.set_pixel(0, 3, eight_row)
            sense.set_pixel(0, 2, eight_row)
            sense.set_pixel(0, 1, eight_row)
            sense.set_pixel(4, 7, blank)
            sense.set_pixel(4, 6, blank)
            sense.set_pixel(4, 5, blank)
            sense.set_pixel(4, 4, blank)
            sense.set_pixel(4, 3, blank)
            sense.set_pixel(4, 2, blank)
            sense.set_pixel(4, 1, blank)
            sense.set_pixel(3, 7, blank)
            sense.set_pixel(3, 6, blank)
            sense.set_pixel(3, 5, blank)
            sense.set_pixel(3, 4, blank)
            sense.set_pixel(3, 3, blank)
            sense.set_pixel(3, 2, blank)
            sense.set_pixel(3, 1, blank)
            sense.set_pixel(2, 7, blank)
            sense.set_pixel(2, 6, blank)
            sense.set_pixel(2, 5, blank)
            sense.set_pixel(2, 4, blank)
            sense.set_pixel(2, 3, blank)
            sense.set_pixel(2, 2, blank)
            sense.set_pixel(2, 1, blank)
        elif distance2 >= HazardThresholdFar:
            sense_hat_ledFarther()
        
            
        
        

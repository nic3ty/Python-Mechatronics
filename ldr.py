from gpiozero import LightSensor, Buzzer
from time import sleep
ldr = LightSensor(24)

while True:
    print(ldr.value)
    sleep(0.5)
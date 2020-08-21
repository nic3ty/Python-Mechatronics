import time
import RPi.GPIO as GPIO
import gpiozero
button = gpiozero.Button(2)
button.wait_for_press()
print("you pushed me")






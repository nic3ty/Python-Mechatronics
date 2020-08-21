from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

if sense.temp > 20.0:
    print("It's pretty hot!")
elif sense.temp < 20.0:
    print("It's not so hot!")

sleep(2)

while True:
    print("Temp from temp:",sense.temp)
    print("Temp from humidity:", sense.get_temperature_from_humidity())#Same sensor as sense.temp
    print("Temp from pressure:", sense.get_temperature_from_pressure())#Inaccurate
    sleep(0.5)
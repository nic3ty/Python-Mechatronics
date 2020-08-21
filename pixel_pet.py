from sense_hat import SenseHat
sense = SenseHat()
from time import sleep


a = (0, 255, 255)
r = (255, 0, 10)
b = (0, 0, 0)
w = (255, 255, 255)

pet1 = [
w, w, w, w, w, w, w, w,
w, w, w, r, r, r, w, w,
w, w, r, r, r, r, w, w,
r, a, a, a, a, a, b, w,
w, a, a, a, a, a, a, w,
w, w, a, a, a, a, w, w,
w, w, a, w, w, a, w, w,
w, w, r, w, w, r, w, w,
]

pet1_2 = [
w, w, w, w, w, w, w, w,
w, w, w, r, r, r, w, w,
w, w, r, r, r, r, w, w,
r, a, a, a, a, a, b, w,
w, a, a, a, a, a, a, w,
w, w, a, a, a, a, w, w,
w, w, w, a, w, w, a, w,
w, w, w, w, r, w, r, w,
]
def walking():
    while True:
        sleep(0.5)
        sense.set_pixels(pet1)
        sleep(0.5)
        sense.set_pixels(pet1_2)
        sleep(0.5)
while True:
    acc = sense.get_accelerometer_raw()
    if acc['x'] > 2 or acc['y'] > 2 or acc['z'] > 2:
        walking()
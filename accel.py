from sense_hat import SenseHat
from time import sleep
import time
sense = SenseHat()
sense.set_imu_config(False, False, True)
start = time.time()
elapsed = 0
while elapsed < 300:
    accel = sense.get_accelerometer_raw()
    x = accel['x']
    y = accel['y']
    z = accel['z']
    print("x={0}".format(round(x, 4)))
    sleep(0.1)
    elapsed = time.time() - start
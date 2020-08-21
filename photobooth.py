from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep
import sys
mc = Minecraft.create()
camera = PiCamera()

mc.postToChat("Initializing...")

while True:
    x, y, z = mc.player.getPos()
    sleep(0.5)
    print(x, y, z)
#    if 6 <= x <= 6.9 and y == 6 and -6 <= z <= -6.9:
    if 7 <= x <= 7.9 and y == 8 and 6 <= z <= 6.9:
        mc.postToChat("You are in the photobooth! Get ready to smile!")
        mc.postToChat("5...")
        sleep(1)
        mc.postToChat("4...")
        sleep(1)
        mc.postToChat("3...")
        sleep(1)
        mc.postToChat("2...")
        sleep(1)
        mc.postToChat("1...")
        sleep(1)
        mc.postToChat("Cheese!")
        camera.capture('/home/pi/photobooth1.jpg')
sys.exit()
from gpiozero import Button, LED

leds = LED(25, 24, 23)
button = Button(21)
while True:
    button.wait_for_press()
    leds.on()
    button.wait_for_release()
    leds.off()
    
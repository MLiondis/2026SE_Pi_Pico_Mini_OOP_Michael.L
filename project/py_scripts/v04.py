from led_light import Led_Light
from time import sleep

red_light = Led_Light(3, True, False)

while True:
    red_light.flash()
    sleep(3)
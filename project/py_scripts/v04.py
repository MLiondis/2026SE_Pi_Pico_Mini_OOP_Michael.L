from led_light import Led_Light
from time import sleep

# sets the Led_Light pins, debuging and flashing for the red led light
red_light = Led_Light(3, True, False)
green_light = Led_Light(6, True, False)
amber_light = Led_Light(5, True, False)

toggle_light = Led_Light(5, True, False)

red_light.on()
print("LED is on")
sleep(3)
red_light.off()
sleep(0.5)

amber_light.on()
print("LED is on")
sleep(3)
amber_light.off()
sleep(0.5)

green_light.on()
print("LED is on")
sleep(3)
green_light.off()
sleep(0.5)

while True:
    print("Flashing")
    red_light.flash()
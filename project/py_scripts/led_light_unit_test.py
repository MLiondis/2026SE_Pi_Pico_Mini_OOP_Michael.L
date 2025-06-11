from led_light import Led_Light
from time import sleep

# sets the Led_Light pins, debuging and flashing for the red led light
red_light = Led_Light(3, True, False)

toggle_light = Led_Light(5, True, False)

red_light.on()
print("LED is on")
sleep(0.5)

red_light.off()
print("LED is off")
sleep(0.5)

print("toggling test now")
toggle_light.toggle()
print("red light is toggling")
if red_light.value == 1:
    print("toggle is on")
sleep(2)
toggle_light.toggle()
print("red light is toggling")
if red_light.value == 0:
    print("toggle is off")

red_light.flash()
print("red light is flashing!")
sleep(2)
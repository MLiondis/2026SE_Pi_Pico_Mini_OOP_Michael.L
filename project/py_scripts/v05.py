from pedestrian_button import Pedestrian_Button
from led_light import Led_Light
from time import sleep

#create a pedestrian button for gpiopin 14
button = Pedestrian_Button(22, debug=True)

led_light = Led_Light(3, True, False)

while True:
    if button.value() == 1:
        led_light.on()
        print("LED is on")
    if button.value() == 0:
        led_light.off()
        print("LED is off")
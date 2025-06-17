from pedestrian_button import Pedestrian_Button
from led_light import Led_Light
from time import sleep

#create a pedestrian button for gpiopin 14
button = Pedestrian_Button(22, debug=False)

led_light = Led_Light(3, True, False)

while True:
    if button.button_state() == 1:
        led_light.on()
        print("LED is on")
        sleep(0.5)
    if button.button_state() == 0:
        led_light.off()
        print("LED is off")
        sleep(0.5)
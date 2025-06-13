from pedestrian_button import Pedestrian_Button
import time

#create a pedestrian button for gpiopin 14
button = Pedestrian_Button(22, debug=True)

while True:
    # waits until the button has been pressed
    if button.button_state:
        #If button pressed prin(), then change the state back to false
        print("A pedestrian is waiting")
        button.button_state = False
    time.sleep(0.5)
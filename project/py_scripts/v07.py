from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep

red_light = Led_Light(3, False, debug=True)
amber_light = Led_Light(5, False, debug=True)
green_light = Led_Light(6, False, debug=True)

P_red_light = Led_Light(19, True, debug=True)
P_green_light = Led_Light(17, True, debug=True)

P_button = Pedestrian_Button(22, debug=True)

P_buzzer = Audio_Notification(27, debug=True)

traffic = TrafficLightSubsystem(red_light, amber_light, green_light, debug=True)
pedestrian = PedestrianSubsystem(P_red_light, P_green_light, P_button, P_buzzer, debug=True)

def Traffic_Subsystem_Driver():

    print("Testing traffic light in 3 seconds")
    sleep(3)
    traffic.show_red()
    print("Red: ON, Green: OFF, Amber: OFF")
    sleep(3)
    traffic.show_amber()
    print("Red: OFF, Green: OFF, Amber: ON")
    sleep(3)
    traffic.show_green()
    print("Red: OFF, Green: ON, Amber: OFF")
    sleep(5)
    green_light.off()

def Pedestrian_Subsystem_Driver():

    print("Testing pedestrian lights in 3 seconds")
    sleep(3)
    pedestrian.show_stop()
    print("Red: ON, Green: OFF")
    sleep(3)
    pedestrian.show_walk()
    print("Red: OFF, Green: ON")
    sleep(3)

    print("testing pedestrian warning in 3 seconds")
    sleep(3)
    while True:
        pedestrian.show_warning()

Traffic_Subsystem_Driver()
Pedestrian_Subsystem_Driver()
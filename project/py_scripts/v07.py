from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notfication import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep

red_light = Led_Light(3, False, debug=True)
amber_light = Led_Light(5, False, debug=True)
green_light = Led_Light(7, False, debug=True)

P_red_light = Led_Light(19, True, debug=True)
P_green_light = Led_Light(17, True, debug=True)

P_button = Pedestrian_Button(22, debug=True)

P_buzzer = Audio_Notification(27, debug=True)

traffic = TrafficLightSubsystem(red_light, amber_light, green_light, debug=True)
pedestrian = PedestrianSubsystem(P_red_light, P_green_light, P_button, P_buzzer, debug=True)

def Subsystem_driver():

    print("Pedestrian is waiting, cars are going")
    traffic.show_green()
    pedestrian.show_stop()
    sleep(5)
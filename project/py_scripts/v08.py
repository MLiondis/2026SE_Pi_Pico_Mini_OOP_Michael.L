from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from time import sleep

red_light = Led_Light(3, False, debug=False)
amber_light = Led_Light(5, False, debug=False)
green_light = Led_Light(6, False, debug=False)

P_red_light = Led_Light(19, True, debug=False)
P_green_light = Led_Light(17, True, debug=False)

P_button = Pedestrian_Button(22, debug=False)

P_buzzer = Audio_Notification(27, debug=False)

traffic = TrafficLightSubsystem(red_light, amber_light, green_light, debug=False)
pedestrian = PedestrianSubsystem(P_red_light, P_green_light, P_button, P_buzzer, debug=False)
system = Controller(P_red_light, P_green_light, red_light, amber_light, green_light, P_button, P_buzzer, debug=False)

def System_driver():
    print("System test")
    sleep(3)
    print("Idle state for 5 seconds")
    system.set_idle_state()
    sleep(5)
    print("Change state for 5 seconds")
    system.set_change_state()
    sleep(5)
    print("Walk state for 5 seconds")
    system.set_walk_state()
    print("Warning state for 5 seconds")
    system.set_warning_state()
    sleep(5)
    print("Error state for 5 seconds")
    system.error_state()
    sleep(5)

System_driver()
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

class TrafficLightSubsystem:
    def __init__(self, red, amber, green, debug=False):
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug

    def show_red(self):
        if self.__debug:
            print("Traffic: Red ON")
        self.__red.on()
        self.__amber.off()
        self.__green.off()

    def show_amber(self):
        if self.__debug:
            print("Traffic: Amber ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()

    def show_green(self):
        if self.__debug:
            print("Traffic: Green ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()

    def show_error(self):
        if self.__debug:
            print("Traffic: Error ON")
        self.__red.off()
        self.__amber.flash()
        self.__green.off()

class PedestrianSubsystem:
    def __init__(self, red, green, button, buzzer, debug=False):
        self.__red = red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug

    def show_stop(self):
        if self.__debug:
            print("Pedestrian: Red ON")
        self.__red.on()
        self.__green.off()
        self.__buzzer.warning_off()

    def show_walk(self):
        if self.__debug:
            print("Pedestrian: Green ON")
        self.__red.off()
        self.__green.on()
        self.__buzzer.warning_on()

    def show_warning(self):
        if self.__debug:
            print("Pedestrian: Warning ON")
            self.__red.flash()
            self.__green.off()
            self.__buzzer.warning_off()

    def is_button_pressed(self):
        return self.__button.button_state()
    
    def reset_button(self):
        self.__button.button_state(False)

class Controller:
    def __init__(self, ped_red, ped_green, car_red, car_amber, car_green, button, buzzer, debug):
        self.__traffic_lights = TrafficLightSubsystem(car_red, car_amber, car_green, debug)
        self.__pedestrian_signals = PedestrianSubsystem(ped_red, ped_green, button, buzzer, debug)
        self.__debug = debug
        self.state = "IDLE"
        self.last_state_change = time()
    
    def set_idle_state(self):
        if self.__debug:
            print("System: IDLE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_green()

    def set_change_state(self):
        if self.__debug:
            print("System: CHANGE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()

    def set_walk_state(self):
        if self.__debug:
            print("System: WALK state")
        self.__pedestrian_signals.show_walk()
        self.__traffic_lights.show_red()

    def set_warning_state(self):
        if self.__debug:
            print("System: WARNING state")
        self.__pedestrian_signals.show_warning()
        self.__traffic_lights.show_red()
    
    def error_state(self):
        if self.__debug:
            print("System: WARNING state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_error()

    def update(self):
        now = time()
        print(self.state)
        if self.state == "IDLE":
            self.set_idle_state()
            if self.__pedestrian_signals.is_button_pressed():
                self.state == "CHANGING"
                print(self.state)
                self.last_state_change = now
        elif self.state == "CHANGING":
            self.set_change_state()
            if time.now() - self.last_state_change >= 10:
                self.last_state_change = now
                sleep(5)
                self.set_walk_state()
                sleep(5)
                self.set_warning_state()
                sleep(3)
        else:
            self.error_state()
from machine import Pin, PWM
from time import sleep, time

class Audio_Notification(PWM):

    """
        A class that sets the a buzzer durations for pedestrians

        Arguments:
            pin(int): GPIO pin number for the LED

        Example:
            duty_u16(int): sets how loud/hard/frequent the buzzer buzzes

            sef.duty_u16(0) # turns the buzzer off
            self.duty_u16(32768) # 50% power/loudness/hardness etc.
    """
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__pin = pin
        self.__debug = debug
        self.duty_u16(0) #starts with buzzer off
        self.__last_toggle_time = time()

    def beep(self, freq=1000, duration=500):
        if self.__debug:
            print("Beep")
        self.freq(freq)
        self.duty_u16(65536) # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0) # turn off ater beep

    def warning_on(self):
        """
            Sets the buzzer to buzz at a certain frequency & duration

            Sets a cooldown time for the buzzer to buzz again
        """
        if self.__debug:
            print("Warning on")
        now = time()
        if now - self.__last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now
    
    def warning_off(self):
        if self.__debug:
            print("Warning off")
        self.duty_u16(0) # turn off the sound
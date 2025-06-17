from machine import Pin
from time import ticks_ms, ticks_diff

class Pedestrian_Button(Pin):
    """
        A class that gives a pedestrian button funcionality with a timer

        Arguments:
            pin(int): GPIO pin number for the LED
        
        Examples:
            button_state() # sets the state of the button to check if theres someone waiting
    """
    def __init__(self, pin, debug):
        #child class inherits the parent 'Pin' class
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0 #tracks last time pressed
        self.__pedestrian_waiting = False
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    def button_state(self, value=None):
            if value is None:
                #getter
                if self.__debug:
                    print(f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}")
                return self.__pedestrian_waiting
            else:
                self.__pedestrian_waiting = bool(value)
                #convert too boolean to ensure proper type 
                if self.__debug:
                    print(f"Button state on Pin {self.__pin} set to {self.__pedestrian_waiting}")

    def callback(self, pin):
        """
            A function that makes it so the button can only pressed/sensed after a certain amount of time
            e.g. it wont overload the system if the pedestrian spams it
        """
        current_time = ticks_ms() # get the current time in miliseconds
        if (ticks_diff(current_time, self.__last_pressed) > 200): #200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
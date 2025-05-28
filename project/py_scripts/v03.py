from machine import Pin, ADC
from time import sleep

#idle to become ready 
sleep(0.1)

#store output pin in a variable
led_pin = 25
led2_pin = 20
data_pin = 13
analog_data_pin = 26

#configure gpio pin as output and create object for pin class
led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

#confugure gpio pin for input
data = Pin(data_pin, Pin.IN)

#configure gpio as adc pin
adc_value = ADC(Pin(analog_data_pin))

while True:
    if data.value() == 1:
        led.value(True)
        led2.value(False)
    else:
        led.value(False)
        led2.value(True)
    print(f"Analog: {adc_value.read_u16()}")
    sleep(0.1)
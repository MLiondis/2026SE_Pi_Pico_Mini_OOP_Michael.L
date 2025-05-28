from machine import Pin
from time import sleep 

#initiation pause
sleep(0.1)

#led output pin
led_pin = 25

#configure the output pin
led = Pin(led_pin. Pin.OUT)

while True:
    led.value(True)
    sleep(1)
    led.value(False)
    sleep(1)
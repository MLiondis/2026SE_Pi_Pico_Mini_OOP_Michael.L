from machine import Pin, ADC, PWM
from time import sleep

#idle to become ready 
sleep(0.1)

#store output pin in a variable
led_pin = 25
led2_pin = 20
data_pin = 13
analog_data_pin = 26
servo_pin = 10

#configure gpio pin as output and create object for pin class
led = PWM(Pin(led_pin))
led2 = PWM(Pin(led2_pin))

#set the pwm frequency for LED's 
led.freq(1000)
led2.freq(1000)

# configure gpio pin for servo
servo = PWM(Pin(servo_pin))

#set frequenct for servo
servo.freq(50)

#confugure gpio pin for input
data = Pin(data_pin, Pin.IN)

#configure gpio as adc pin
analog_data = ADC(Pin(analog_data_pin))

#func to calculate pulse width in microseconds 
def set_angle(angle):
    #makes the imput angle 0-180
    angle = min(max(angle, 0), 180)
    #return the angle value in terms of the servo's units
    return int(500 + (angle / 180) * 2000)

#function to linearly map values
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


while True:
    adc_value = analog_data.read_u16() # 0-65535
    if data.value() == 1:
        led.duty_u16(adc_value)
        led2.duty_u16(adc_value)
    else:
        led.duty_u16(0)
        led2.duty_u16(0)
    mapped_value = map_range(adc_value, 0, 65535, 0, 180)
    servo.duty_ns(set_angle(mapped_value) * 1000)
    print(f"Digital: {data.value()} ,  Analog: {adc_value} , Servo: {servo.duty_ns()}")
    sleep(0.1)
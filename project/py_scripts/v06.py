from machine import Pin, PWM, time_pulse_us
from time import sleep, sleep_us

#idle to become ready 
sleep(0.1)

#store output pin in a variable
TRIG_PIN = 12
ECHO_PIN = 11
servo_pin = 10

# configure gpio pin for servo
servo = PWM(Pin(servo_pin))

#set frequenct for servo
servo.freq(50)

#config echo and trig
trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

#func to calculate pulse width in microseconds 
def set_angle(angle):
    #makes the imput angle 0-180
    angle = min(max(angle, 0), 180)
    #return the angle value in terms of the servo's units
    return int(500 + (angle / 180) * 2000)

#function to linearly map values
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def get_distance():
    # send a pulse to trigger
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    #wait for echo, measure the duration
    try:
        pulse_time = time_pulse_us(echo, 1, 30000) #wait for high
    except OSError as ex:
        if ex.args[0] == 110: # timeout
            return None
        raise ex
    
    #calc distance
    distance_cm = (pulse_time / 2) / 29.1
    return distance_cm

while True:
    dist = get_distance
    if dist is not None:
        mapped_value = map_range(dist, 0, 410, 0, 180)  #adjusts range as needed
        servo.duty_ns(set_angle(mapped_value) * 1000)
    else: 
        print("Out of range")
    print(f"Distance: {dist} , Servo: {servo.duty_ns()}")
    sleep(0.1)
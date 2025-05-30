from machine import I2C, Pin, time_pulse_us, PWM
from time import sleep, sleep_us

# very important
# this module needs to be saved in the rasberry PI pico for it to be used
from pico_i2c_lcd import I2cLcd


#store desired output pins in a variable
TRIG_PIN = 12
ECHO_PIN = 11

#configure Echo & Trig GPIO Pins as objects for Pin class
trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

#create I2C object
# any sda and scl pins in the raspberry pi pico can be user
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

#get I2C address
I2C_ADDR = i2c.scan()[0]

# create an LCD object using the i2c address and specify number of rows and columns in the lcd 
# LCD number of rows = 2, number of rows = 16
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def get_distance():
    # Send a 10us pulse to trigger
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    # Wait for echo, measure the duration
    try:
        pulse_time = time_pulse_us(echo, 1, 30000)  # Wait for HIGH
    except OSError as ex:
        if ex.args[0] == 110:  # Timeout
            return None
        raise ex

    # Calculate distance (speed of sound = 340 m/s)
    distance_cm = (pulse_time / 2) / 29.1
    return distance_cm

while True:
    dist = get_distance()
    #putstr method allows printing of text on the LCD screen
    # for other methods that can be used, check lcd_api module
    print(dist)
    lcd.putstr(f"Distance: {dist}")
    sleep(0.1)
    lcd.clear()
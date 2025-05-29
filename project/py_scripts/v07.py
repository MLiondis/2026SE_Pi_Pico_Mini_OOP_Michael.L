from machine import I2C, Pin,
from time import sleep

# very important
# this module needs to be saved in the rasberry PI pico for it to be used
from pico_i2c_lcd import I2cLcd

#create I2C object
# any sda and scl pins in the raspberry pi pico can be user
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

#get I2C address
I2C_ADDR = i2c.scan()[0]

# create an LCD object using the i2c address and specify number of rows and columns in the lcd 
# LCD number of rows = 2, number of rows = 16
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

#continuously print and clear "hello world" text in the lcd screen

while True:
    #putstr method allows printing of text on the LCD screen
    # for other methods that can be used, check lcd_api module
    lcd.putstr("Matcha")
    sleep(5)  # matcha will disply for 5 sec
    lcd.clear()
    sleep(1)  # clear txt for 1 sec the print txt again
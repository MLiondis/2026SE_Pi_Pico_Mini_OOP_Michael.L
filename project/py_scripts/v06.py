from audio_notification import Audio_Notification
from time import sleep

#make the buzzer connect the pin on the pico and set the debug to true
buzzer = Audio_Notification(27, debug=True)

timer = 10
while True:
#make the buzzer turn on for the time allocated in the func
    buzzer.warning_on()
    sleep(1)
    if timer < 4:
        sleep(0.5)
    if timer < 2:
        sleep(0.25)
    if timer < 1:
        buzzer.warning_on()
        buzzer.warning_off()
    timer -= 1

# turn the buzzer off again
buzzer.warning_off()
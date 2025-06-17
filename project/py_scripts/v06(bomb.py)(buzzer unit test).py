from audio_notification import Audio_Notification
from time import sleep

#make the buzzer connect the pin on the pico and set the debug to true
buzzer = Audio_Notification(27, debug=True)

timer = 20
while True:
#make the buzzer turn on for the time allocated in the func
    buzzer.beep(500, 100)
    if timer >= 15:
        sleep(2)
    if timer >= 10:
        sleep(1)
    if timer >= 5:      
        sleep(0.5)
    elif timer <= 5:
        while True:
            buzzer.beep(500, 90)
            sleep(0.1)
    timer -= 1
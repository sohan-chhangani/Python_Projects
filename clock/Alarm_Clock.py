import datetime
from playsound import playsound
alarm_hr = int(input("Enter Hour: ")) 
alarm_min = int(input("Enter Minutes: "))
alarm_day = input("Enter Am/Pm: ")

if alarm_day=="pm":
    alarm_hr+=12

while True:
    if alarm_hr == datetime.datetime.now().hour and alarm_min==datetime.datetime.now().minute:
        print("Playing...")
        playsound("sound.mp3")
        break
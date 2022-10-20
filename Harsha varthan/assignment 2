import random
import winsound
import time


while True:
    temperature =random.randint(-68,49) 
    humidity = random.randint(0,100) 
    print(f"Temperature = {temperature}C ------- Humidity = {humidity}%")
    if temperature>35 and humidity >50:
        for i in range(10):
            winsound.Beep(1000,10)
        print("Alarm is ON")
    else:
        print("Alarm is OFF")
    time.sleep(10)

    print()
    print()

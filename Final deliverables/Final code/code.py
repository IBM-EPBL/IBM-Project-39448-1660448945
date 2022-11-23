import wiotp.sdk.device
import time
import random
import requests, json
# give your credentials below
myConfig = { 
    "identity": {
        "orgId": "",
        "typeId": "",
        "deviceId":" "
    },
    "auth": {
        "token": " "


    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Coimbatore"
URL = BASE_URL + "q=" + "Coimbatore" + "&appid=" + "  "

while True:
    response = requests.get(URL)
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       temperature = main['temp']
       humidity = main['humidity']
       pressure = main['pressure']
       report = data['visibility']
       repo=random.randint(0,5)
       if repo==1:
           prt="SLOW DOWN , SCHOOL IS NEAR"
       elif repo==3:
           prt="SLOW DOWN , HOSPITAL NEARBY"
       elif repo==5:
           prt="NEED HELP, POLICE STATION NEARBY"
       else:
            prt=""
       speed=random.randint(0,150)
       if speed>=100:
           prt3="SLOW DOWN , Speed Limit Exceeded"
       elif speed>=60 and speed<100:
           prt3="Moderate Speed"
       else:
            prt3="Usual speed limit"
       sign=random.randint(0,5)
       if sign==1:
           prt2="Right Diversion ->"
       elif sign==3:
           prt2="Left Diversion <-"
       elif sign==5:
           prt2="U Turn"
       else:
            prt2=""
       if temperature<=50:
           prt4="Fog Ahead, Drive Slow"
       else:
            prt4="Clear Weather"

    else:
       print("Error in the HTTP request")
    myData={'Temperature':temperature,'Humidity':humidity,'Pressure':pressure, 'Message':prt, 'Sign':prt2, 'Speed':prt3, 'Visibility':prt4}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(5)
client.disconnect()

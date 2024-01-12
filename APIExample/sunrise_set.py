from tkinter import *
import requests
from datetime import datetime


MY_LAT = 51.507351
MY_LONG = -0.127758

url ="https://api.sunrise-sunset.org/json"



parameters = {
     "lat":MY_LAT,
     "lng":MY_LONG,
}



response = requests.get(url,params=parameters)



response.raise_for_status()
data = response.json()




print(response)
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
#print(sunset.split("1")[1].split(":")[0])

time_now = datetime.now()

print(time_now)






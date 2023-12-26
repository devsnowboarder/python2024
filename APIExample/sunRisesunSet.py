

import requests
import pprint
from datetime import datetime

MY_LAT = 51.507
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
print(reponse.status_code)
data = reponse.json()
print(data)
print(data["results"])

sunrise = data["results"]["sunrise"]
print(sunrise.split("T")[1].split(":")[1])

sunset = data["results"]["sunset"]
print(sunset)
print(sunset.split("T")[1].split(":")[0])



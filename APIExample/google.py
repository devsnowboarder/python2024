
import requests

URL = "https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123"

sample_body =  {
  "location": {
    "lat": -38.383494,
    "lng": 33.427362
  },
  "accuracy": 50,
  "name": "Frontline house",
  "phone_number": "(+91) 983 893 3937",
  "address": "29, side layout, cohen 09",
  "types": [
    "shoe park",
    "shop"
  ],
  "website": "http://google.com",
  "language": "French-IN"
}


url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

response = requests.post(url, myobj)

response = requests.get(url)
print(response.status_code)
print(response.json())


response = requests.post(URL, sample_body)
print(response.status_code)

response = requests.post(URL)
#print(response.json())




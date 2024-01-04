import requests
import pprint

URL ="https://pstmn-api-101.herokuapp.com/customers"

URLGET ="https://pstmn-api-101.herokuapp.com/customer?id=1"

reponse = requests.get(URL)
print(reponse.status_code)
print(reponse.raise_for_status())
data = reponse.json()
#print(data)
print(data['welcome'])
print(data['data'])
print(data['data']['customers'])

for x in range(3):
   print(data['data']['customers'][x]['name'])
   print(data['data']['customers'][x]['type'])

reponse = requests.get(URLGET)
print(reponse.status_code)
print(reponse.raise_for_status())
data = reponse.json()
print(data)
print(data['data'])
print(data['data']['customer'])




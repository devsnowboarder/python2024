from tkinter import *
import requests



response = requests.get("https://api.kanye.rest")
response.raise_for_status()
data = response.json()
quote = data["quote"]



print(response)
print(data)
print(quote)



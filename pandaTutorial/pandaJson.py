import jason as jason
import pandas as pd
import json


df = open('data.json')
df = jason.load()

print(df)


import pandas as pd


pd.options.display.max_rows = 999

df = pd.read_csv('vgsales.csv')
9
print(df.describe())

df.values

print(df.shape)

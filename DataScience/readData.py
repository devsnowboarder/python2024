import pandas as pd

df = pd.read_csv("/Users/michaellau/python2024/python2024/DataScience/order.csv")
print(df.to_string())

new_df = df.dropna()
print(new_df.to_string())


df.fillna(100, inplace=True)
print(df.to_string())


df_new = df.drop_duplicates()

print("===============  droping duplicates")

print(df_new.to_string())
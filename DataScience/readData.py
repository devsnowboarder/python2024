import merged as merged_data
import pandas as pd

df = pd.read_csv("/Users/michaellau/python2024/python2024/DataScience/order.csv")
print(df.to_string())

merged_data.to_csv("/Users/michaellau/python2024/python2024/DataScience/output.csv")

#new_df = df.dropna()
#print(new_df.to_string())


#df.fillna(100, inplace=True)
#print(df.to_string())





df_new = df.drop_duplicates()

print("===============  droping duplicates")

print(df_new.to_string())



#df["order_date"] = pd.to_datetime(df["order_date"], format = '%d%m%y')


avg_sale  = new_df.groupby('ItemType')['UnitsSold'].mean()

print(avg_sale)

print(new_df.aggregate(['sum','min','max']))






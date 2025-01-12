
import pandas as pd
import  matplotlib.pyplot as plt


data ={'Date': ['2023-08-01','2023-08-02','2023-08-03'],
       'Price':[100,105,110]}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

df.plot(x = 'Date', y = 'Price', kind = 'line')

plt.xlabel('Data')
plt.ylabel('Price')
plt.show()
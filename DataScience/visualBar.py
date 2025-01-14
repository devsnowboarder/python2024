import pandas as pd
import  matplotlib.pyplot as plt

data = {'Product': ['A','B','C'],
         'Sales' : [500,750,300]}

df = pd.DataFrame(data)

df.plot(x = 'Product', y = 'Sales', kind = 'bar')
plt.xlabel('Product')
plt.ylabel('Sales')

plt.show()
import pandas as pd
import  matplotlib.pyplot as plt

data = {'Topping': ['Pepperoni', 'Mushroom', 'Olive', 'Sausage'],
        'Count': [25, 15, 10, 20]}
df = pd.DataFrame(data)

df.plot(x = 'Topping', y = 'Count', kind ='pie')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vgsales.csv')

print(df.info())

df.plot()

plt.show()
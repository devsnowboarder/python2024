import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

print(df.info())

df.plot()

plt.show()
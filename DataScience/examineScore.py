import pandas as pd
import  matplotlib.pyplot as plt

data = {'Hours_Studied': [2,4,5,7,8,10],
         'Exam_Score' : [60,70,75,85,90,95]}
df = pd.DataFrame(data)

df.plot(x ='Hours_Studied', y ='Exam_Score', kind = 'scatter')
plt.xlabel('Hours_Studied')
plt.ylabel('Exam_Score')

plt.show()
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

pd.options.display.max_rows = 99999

music_data = pd.read_csv('music.csv')
9
print(music_data)

X = music_data.drop(columns=['genre'])
y = music_data['genre']

print(X)
print(y)

model = DecisionTreeClassifier()
model.fit(X, y)
predictions = model.predict([[21, 1], [22, 0]])
predictions

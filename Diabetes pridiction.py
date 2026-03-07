#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns#to visualize data
#load data set
df = pd.read_csv("diabetes.csv")
print(df.head())# first 5 rows read krna kaliya
#EDA
df.shape#rows and column
df.columns#features
df.info()#data type
df.describe()# mean,min,max ,standard deviation
df.isnull().sum()#null rows and column
#correlation heatmap
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,8))#for set plot size
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
#Target variable distribution/data scaling
df["Outcome"].value_counts()
x = df.drop("Outcome",axis=1)
y =df["Outcome"]
#test train split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2, random_state=42)
print("Model training start")
model.fit(x_train, y_train)
print("Model training done")

y_pred = model.predict(x_test)
print("Prediction done")

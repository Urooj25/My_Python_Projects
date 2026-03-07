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
#train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#Model training
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Starting model training...")

# 1️⃣ Model create
model = LogisticRegression(max_iter=1000)

# 2️⃣ Train model
model.fit(x_train, y_train)
print("Training done")

# 3️⃣ Predict on test data
y_pred = model.predict(x_test)
print("Prediction done")

# 4️⃣ Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# Confusion matrix plot
ConfusionMatrixDisplay.from_estimator(model, x_test, y_test, cmap="Blues", display_labels=["Non-Diabetic", "Diabetic"])
plt.show()
import joblib


# Load model
loaded_model = joblib.load("diabetes_model.pkl")

# Predict on new data
new_data = [[2, 120, 70, 30, 100, 25.5, 0.5, 33]]  # example
prediction = loaded_model.predict(new_data)

print("Prediction:", "Diabetic" if prediction[0]==1 else "Non-Diabetic")
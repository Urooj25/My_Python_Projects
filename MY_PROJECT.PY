import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import matplotlib.pyplot as plt

# 1️⃣ CSV load karo
data = pd.read_csv("StudentsPerformance.csv")

# 2️⃣ Average score calculate
data['average_score'] = data[['math score','reading score','writing score']].mean(axis=1)

# 3️⃣ Features and target
X = data[['math score','reading score','writing score']]  # simple example
y = data['average_score']

# 4️⃣ Model train
model = LinearRegression()
model.fit(X, y)

# 5️⃣ Model save
with open("student_model.pkl","wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")

# 6️⃣ Predictions aur graph
predictions = model.predict(X)
plt.scatter(y, predictions)
plt.xlabel("Actual Average Score")
plt.ylabel("Predicted Average Score")
plt.title("Actual vs Predicted Scores")
plt.show()
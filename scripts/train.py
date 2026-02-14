import json
import joblib
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, mean_squared_error

X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

preds = model.predict(X_test)

f1 = f1_score(y_test, preds, average="weighted")
mse = mean_squared_error(y_test, preds)

joblib.dump(model, "model.joblib")

metrics = {
    "f1": float(f1),
    "mse": float(mse)
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)

accuracy = (preds == y_test).mean()
precision = (preds[y_test == 1] == 1).mean()
recall = (y_test[preds == 1] == 1).mean()

# print("Metrics:", metrics)
print("Name: Khushi Jain")
print("Roll No: 2022BCS0130")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

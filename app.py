from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.joblib")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict():
    dummy_input = np.random.rand(1, 13)
    pred = model.predict(dummy_input)[0]

    return {
        "name": "Khushi Jain",
        "roll_no": "YOUR_ROLL_NO",
        "wine_quality": int(pred)
    }

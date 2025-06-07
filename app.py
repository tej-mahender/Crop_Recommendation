from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')

# Load models once at startup
with open(os.path.join(MODEL_DIR, 'yield_model.pkl'), 'rb') as f:
    yield_model = pickle.load(f)
with open(os.path.join(MODEL_DIR, 'scaler_yield.pkl'), 'rb') as f:
    yield_scaler = pickle.load(f)

with open(os.path.join(MODEL_DIR, 'companion_kmeans.pkl'), 'rb') as f:
    companion_model = pickle.load(f)

# Add other models/scalers as needed...

class YieldPredictionInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    # add all necessary input features here

@app.post("/predict/yield")
def predict_yield(data: YieldPredictionInput):
    try:
        input_arr = np.array([[data.feature1, data.feature2, data.feature3]])
        input_scaled = yield_scaler.transform(input_arr)
        prediction = yield_model.predict(input_scaled)
        return {"predicted_yield": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/recommend/companion")
def recommend_companion(crop_name: str):
    try:
        # Assuming you have a function to get companion crops, e.g.:
        companions = get_companion_crops(crop_name)
        return {"companions": companions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_companion_crops(crop_name):
    # Dummy logic: replace with your actual recommendation code
    # For example, query the kmeans model results stored in a file or memory
    # This is just a placeholder
    return ["crop1", "crop2", "crop3"]

# Similar endpoints for other models

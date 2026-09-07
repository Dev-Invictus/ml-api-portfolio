from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load the trained model once at startup
model = joblib.load("iris_model.pkl")

# Iris species names (matches sklearn's label order: 0, 1, 2)
species_names = ["setosa", "versicolor", "virginica"]

@app.get("/")
def read_root():
    return {"message": "Hello from my ML API portfolio project"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    return {"predicted_species": species_names[prediction]}
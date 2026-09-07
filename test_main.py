from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from my ML API portfolio project"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    response = client.get("/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2")
    assert response.status_code == 200
    assert response.json()["predicted_species"] == "setosa"
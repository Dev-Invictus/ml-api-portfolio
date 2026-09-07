# ML API Portfolio

A machine learning API built with FastAPI, containerized with Docker, and deployed live on Render. This project demonstrates a full ML deployment pipeline — from model training to a publicly accessible prediction endpoint.

**Live demo:** https://ml-api-portfolio.onrender.com

## What it does

This API serves predictions from a trained `RandomForestClassifier` on the classic Iris flower dataset, classifying flowers into one of three species (setosa, versicolor, virginica) based on four measurements.

## Tech stack

- **FastAPI** — web framework for the API
- **scikit-learn** — model training (RandomForestClassifier)
- **Docker** — containerization
- **Render** — cloud deployment (auto-deploys from GitHub on push)
- **GitHub Codespaces** — cloud development environment

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check / welcome message |
| GET | `/health` | Simple status check |
| GET | `/predict` | Returns predicted iris species |

### Example request

### Example response

```json
{"predicted_species": "setosa"}
```

## Running locally

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model (generates iris_model.pkl)
python3 train_model.py

# Run the API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Running with Docker

```bash
docker build -t ml-api-portfolio .
docker run -p 8000:8000 ml-api-portfolio
```

## Project structure

## Author

Built as a portfolio project for exploring AI DevOps / MLOps workflows — cloud-based development, containerization, and CI/CD-style deployment.
# D2C Customer Churn Prediction API

Production-ready FastAPI service for predicting customer churn in a Direct-to-Consumer (D2C) business using a trained Random Forest Machine Learning model.

---

## Overview

This project exposes a machine learning model through a FastAPI REST API.

The API accepts customer behavioral, engagement, support, loyalty, and transaction features and returns:

- Churn Prediction (0 or 1)
- Churn Probability
- Risk Explanation
- Batch Predictions

The goal is to help businesses identify customers likely to churn and take proactive retention actions.

---

## Business Problem

Customer acquisition costs are significantly higher than customer retention costs.

When customers stop engaging or purchasing, businesses lose future revenue and customer lifetime value (CLV).

This API helps retention and marketing teams:

- Identify customers at risk of churning
- Prioritize retention campaigns
- Improve customer lifetime value
- Reduce customer attrition

---

## Features

- FastAPI REST API
- Health Check Endpoint
- Single Customer Prediction
- Batch Customer Prediction
- Churn Probability Score
- Human-readable Risk Categorization
- Automated Testing using Pytest
- Swagger Documentation
- Production-ready Project Structure

---

## Technology Stack

### Backend

- FastAPI
- Uvicorn
- Pydantic

### Machine Learning

- Scikit-learn
- Random Forest Classifier
- Joblib

### Testing

- Pytest
- FastAPI TestClient

---

## Project Structure

```text
d2c-churn-api/
│
├── app/
│   └── main.py
│
├── models/
│   └── model.pkl
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── monitoring_plan.md
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd d2c-churn-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

**GET /health**

Response:

```json
{
  "status": "ok"
}
```

---

### Single Customer Prediction

**POST /predict**

Example Response (values will vary depending on input):

```json
{
  "churn_prediction": 0,
  "churn_probability": 0.2654,
  "risk_explanation": "Low churn risk"
}
```

---

### Batch Prediction

**POST /batch_predict**

Example Response (values will vary depending on input):

```json
{
  "predictions": [
    {
      "churn_prediction": 0,
      "churn_probability": 0.2654,    
      "risk_explanation": "Low churn risk"
    }
  ]
}
```

---

## Risk Interpretation

| Churn Probability | Risk Level |
|-------------------|------------|
| Less than 0.50 | Low churn risk |
| 0.50 to 0.79 | Medium churn risk |
| 0.80 and above | High churn risk |

---

## Model Information

### Algorithm

Random Forest Classifier

### Inputs

The model uses customer-level features such as:

- Recency
- Frequency
- Monetary Value
- Product Views
- Cart Activity
- Email Engagement
- Support Tickets
- Loyalty Tier
- Acquisition Channel
- Product Preferences

### Outputs

- churn_prediction
- churn_probability
- risk_explanation

---

## Testing

Run tests:

```bash
python -m pytest -s
```

Expected Result:

```text
3 passed
```

Validated Endpoints:

- /health
- /predict
- /batch_predict

---

## Monitoring Plan

Recommended production monitoring metrics:

- API Response Time
- Request Volume
- Error Rate
- Churn Probability Distribution
- Data Drift
- Model Performance Drift

---

## Future Improvements

- Docker Containerization
- AWS Deployment
- Azure Deployment
- GCP Deployment
- CI/CD Pipeline
- Authentication & Authorization
- Rate Limiting
- Model Versioning
- Drift Detection Dashboard

---

## Results

Successfully deployed a trained machine learning churn prediction model through a FastAPI service with:

- Real-time scoring
- Batch scoring
- Automated tests
- Production-ready API architecture

---

## Author

Developed as part of an end-to-end Machine Learning Capstone Project focused on:

- Customer Churn Prediction
- Model Deployment
- MLOps Fundamentals
- Production API Development
from fastapi import FastAPI
import uvicorn
from pathlib import Path
import joblib
from schema.user_input import CustomerData

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'model' / 'LogRegression.pkl'

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title='Customer Churn Prediction API',
    description='Predict Customer Churn using Logistic Regression (applied SMOTENC)',
    version='1.0.0'
)

@app.get('/')
def home():
    return {'message': 'Welcome to the Customer Churn Prediction API'}

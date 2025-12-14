import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from fastapi import FastAPI
from pydantic import BaseModel

class SalaryRequest(BaseModel):
    work_year: int
    experience_level: str
    employment_type: str
    job_title: str
    salary_currency: str
    employee_residence: str
    remote_ratio: int
    company_location: str
    company_size: str

app = FastAPI()

example_input = {
    'work_year': 2025,
    'experience_level': 'SE',
    'employment_type': 'FT',
    'job_title': 'Data Scientist',
    'salary_currency': 'USD',
    'employee_residence': 'US',
    'remote_ratio': 100,
    'company_location': 'US',
    'company_size': 'M'
}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/predict")
def predict(input_data: SalaryRequest):
    return {"prediction": float(predict_salary(input_data.dict()))}

model = CatBoostRegressor()
model.load_model('model.cbm')

feature_cols = [
    'work_year',
    'experience_level',
    'employment_type',
    'job_title',
    'salary_currency',
    'employee_residence',
    'remote_ratio',
    'company_location',
    'company_size'
]

def predict_salary(input_data: dict):
    prediction_df = pd.DataFrame([input_data])[feature_cols]
    prediction = model.predict(prediction_df)
    return prediction[0]


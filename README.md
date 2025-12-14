# Salary Prediction API

FastAPI-based salary prediction service using CatBoost machine learning model.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure `model.cbm` is in the root directory

3. Run locally:
```bash
uvicorn run:app --reload
```

4. Access API docs at: `http://localhost:8000/docs`

## API Endpoints

- `GET /` - Health check
- `POST /predict` - Predict salary based on job features

### Example Request:
```json
{
  "work_year": 2025,
  "experience_level": "SE",
  "employment_type": "FT",
  "job_title": "Data Scientist",
  "salary_currency": "USD",
  "employee_residence": "US",
  "remote_ratio": 100,
  "company_location": "US",
  "company_size": "M"
}
```

## Deployment

See deployment instructions for:
- Render
- Railway
- Hugging Face Spaces
- Heroku


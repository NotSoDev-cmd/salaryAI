# Deployment Guide

## Option 1: Render (Recommended - Free Tier Available)

### Steps:
1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/salary-prediction-api.git
   git push -u origin main
   ```

2. **Go to [Render.com](https://render.com)** and sign up/login

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository

4. **Configure:**
   - **Name:** salary-prediction-api
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn run:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free (or paid for better performance)

5. **Add Environment Variables (if needed):**
   - None required for basic setup

6. **Deploy!**
   - Render will automatically deploy when you push to GitHub
   - Your API will be live at: `https://your-app-name.onrender.com`

### Important Notes:
- Free tier spins down after 15 minutes of inactivity (first request may be slow)
- Model file (`model.cbm`) should be committed to GitHub (or use cloud storage)

---

## Option 2: Railway (Easy & Fast)

### Steps:
1. **Push code to GitHub** (same as above)

2. **Go to [Railway.app](https://railway.app)** and sign up

3. **New Project → Deploy from GitHub**
   - Select your repository
   - Railway auto-detects Python

4. **Configure:**
   - Railway will auto-detect `requirements.txt`
   - Start command: `uvicorn run:app --host 0.0.0.0 --port $PORT`
   - Or use the `railway.json` config file

5. **Deploy!**
   - Automatic deployment on git push
   - Get your URL: `https://your-app-name.up.railway.app`

---

## Option 3: Hugging Face Spaces (Great for ML Apps)

### Steps:
1. **Create a new Space on [Hugging Face](https://huggingface.co/spaces)**
   - Choose "Gradio" or "Docker" SDK

2. **Upload files:**
   - `run.py` (rename to `app.py` if using Gradio)
   - `requirements.txt`
   - `model.cbm`
   - `README.md`

3. **For FastAPI, use Docker:**
   Create `Dockerfile`:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "7860"]
   ```

4. **Deploy!**
   - Auto-deploys on push
   - URL: `https://your-username-salary-prediction.hf.space`

---

## Option 4: Heroku (Classic, Now Paid)

### Steps:
1. **Install Heroku CLI** and login
2. **Create `Procfile`** (already created)
3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

---

## Option 5: DigitalOcean App Platform

1. Connect GitHub repo
2. Select Python buildpack
3. Set start command: `uvicorn run:app --host 0.0.0.0 --port $PORT`
4. Deploy!

---

## Testing Your Deployment

Once deployed, test your API:

```bash
curl -X POST "https://your-app-url.com/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "work_year": 2025,
       "experience_level": "SE",
       "employment_type": "FT",
       "job_title": "Data Scientist",
       "salary_currency": "USD",
       "employee_residence": "US",
       "remote_ratio": 100,
       "company_location": "US",
       "company_size": "M"
     }'
```

Or visit: `https://your-app-url.com/docs` for interactive API docs!

---

## Important Notes:

1. **Model File Size:**
   - If `model.cbm` is large (>100MB), consider:
     - Using Git LFS (Large File Storage)
     - Storing in cloud storage (S3, etc.) and downloading on startup
     - Using a CDN

2. **Environment Variables:**
   - Add any secrets via platform's environment variable settings
   - Never commit API keys or secrets to GitHub

3. **Monitoring:**
   - Most platforms provide logs and monitoring
   - Set up alerts for errors

4. **Scaling:**
   - Free tiers have limits
   - Upgrade for production workloads

---

## Quick Start (Recommended: Render)

1. Push to GitHub
2. Sign up at render.com
3. Connect repo
4. Deploy!
5. Done! 🎉


# Deployment Guide

## Prerequisites

- Python 3.11+
- Git

## Install Dependencies

pip install -r requirements.txt

## Backend

set PYTHONPATH=.\backend

uvicorn app.main:app --reload

Backend URL

http://127.0.0.1:8000

Swagger

http://127.0.0.1:8000/docs

## Frontend

cd frontend

streamlit run app.py

Frontend URL

http://localhost:8501

## APIs

Total APIs: 24

## Troubleshooting

### Port Already In Use

Change port number or stop existing service.

### Model Not Found

Run:

POST /predict/train

### Database Issue

Delete supply_chain.db and restart application.
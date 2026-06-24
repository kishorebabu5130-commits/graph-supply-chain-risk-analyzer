# Graph-Based Supply Chain Risk Analyzer

## Project Overview

Graph-Based Supply Chain Risk Analyzer is an AI-powered system that analyzes supplier networks, predicts supplier risk, performs graph analytics, and provides executive dashboards for decision-making.

## Features

- Supplier Management
- Dependency Management
- Graph Analytics
- Risk Prediction using Machine Learning
- Dashboard Analytics
- Reporting and CSV Export
- Streamlit Frontend Dashboard

## Technology Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite

### Graph Analytics
- NetworkX

### Machine Learning
- Scikit-Learn
- Random Forest

### Frontend
- Streamlit

## Project Structure

graph-supply-chain-risk-analyzer

backend/
frontend/
docs/
deployment/
graph/
ml/

## Installation

### Clone Repository

git clone <repository-url>

### Install Dependencies

pip install -r requirements.txt

### Run Backend

set PYTHONPATH=.\backend

uvicorn app.main:app --reload

### Run Frontend

cd frontend

streamlit run app.py

## API Count

Total APIs: 24

## Team Members

- Kishore (Team Lead)
- Predeepa
- Shalini

## Future Scope

- Neo4j Integration
- Real-Time Risk Monitoring
- AI-Based Supply Chain Optimization
- Cloud Deployment
# AI-Powered Smart City Civic Intelligence Platform

An AI-driven smart city platform designed to automatically analyze and prioritize civic complaints using machine learning and real-time analytics.

This system helps municipal authorities identify urgent issues, monitor infrastructure problems, and improve response time for public services.

---

# Live Demo

Deployment in progress.

The application will be accessible through a public link once deployed.

---

# Project Overview

Urban areas receive thousands of complaints related to roads, water supply, sanitation, electricity, and public safety.  

Manual prioritization of these complaints often delays responses to critical issues.

This project introduces an **AI-powered civic complaint prioritization system** that automatically analyzes complaint descriptions and assigns urgency levels.

The system provides a **command center dashboard** for administrators to monitor city issues in real time.

---

# Key Features

## Citizen Interface

- Submit civic complaints
- Upload complaint images
- AI-based complaint priority prediction
- Severity score estimation
- Risk type classification
- Complaint history tracking

---

## Admin Command Center

- Real-time complaint monitoring
- Priority-based complaint filtering
- Complaint category analytics
- Smart city dashboard
- Geographic complaint mapping
- Risk zone identification
- Complaint status management

---

# AI Capabilities

The platform integrates several AI-based analysis features.

### Natural Language Processing

- Complaint text processing
- TF-IDF feature extraction
- Machine learning priority classification

### Severity Scoring

Each complaint receives a severity score indicating urgency.

### Complaint Similarity Detection

The system detects complaints similar to previously reported issues.

### Image Hazard Detection

Uploaded images are analyzed for potential risk indicators.

---

# Technology Stack

## Backend

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt

---

## Machine Learning

- Scikit-learn
- TF-IDF Vectorization
- Machine Learning Classification Models

---

## Data Visualization

- Chart.js dashboards
- Folium interactive maps

---

## Database

- SQLite (development database)

---

## Deployment

- Render cloud hosting

---

# System Architecture

Citizen Complaint Submission  
↓  
Flask Web Application  
↓  
AI Priority Prediction Model  
↓  
Database Storage  
↓  
Admin Command Center Dashboard  

---

## Project Structure

```plaintext
civic-ai-portal
│
├── app
│   ├── admin                # Admin dashboard and complaint management
│   ├── auth                 # Authentication (login, register, reset password)
│   ├── user                 # User dashboard and complaint submission
│   │
│   ├── ai                   # AI priority prediction logic
│   ├── ml                   # Machine learning models and utilities
│   │
│   ├── models               # Database models
│   ├── utils                # Utility functions
│   │
│   ├── static               # CSS, JS and uploaded complaint images
│   │   └── uploads
│   │
│   ├── templates            # HTML templates
│   │   ├── admin
│   │   ├── auth
│   │   └── user
│   │
│   ├── config.py            # Application configuration
│   ├── extensions.py        # Flask extensions
│   └── __init__.py          # App factory
│
├── migrations               # Database migration files
│
├── requirements.txt         # Python dependencies
├── Procfile                 # Server startup configuration
├── render.yaml              # Render deployment configuration
├── run.py                   # Application entry point
└── README.md
```

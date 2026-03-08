# AI Powered Civic Grievance Prioritization System for Smart Urban Governance

This project is an AI-based civic complaint management system designed to assist municipalities in prioritizing public grievances using machine learning and natural language processing.

The system allows citizens to submit complaints and automatically analyzes them using AI to determine urgency, detect risk levels, and assist administrators in efficient urban governance.

---
## Live Demo

You can access the deployed system here:

https://civic-ai-portal.onrender.com

Demo Credentials:

Admin  
username: admin@test.com 
password: admin123

User  
username: user@test.com
password: user123
## Key Features

- User authentication (Login / Registration)
- Complaint submission with location and media upload
- AI-based complaint priority prediction
- Risk classification of civic issues
- Similar complaint detection using NLP
- Image-based risk detection
- Admin dashboard for complaint management
- Complaint analytics and statistics
- Smart-city complaint monitoring system
- Cloud deployment for live demonstration

---

## AI Components

The system integrates several AI modules:

### 1. Complaint Priority Prediction
A machine learning model analyzes the complaint description and predicts its urgency level:
- High Priority
- Medium Priority
- Low Priority

### 2. Risk Classification
The system classifies complaints into risk categories such as:
- Critical Safety
- Moderate Risk
- General Issue

### 3. Similar Complaint Detection
Natural Language Processing (TF-IDF + Cosine Similarity) is used to detect previously submitted complaints with similar descriptions.

### 4. Image Risk Detection
Uploaded images are analyzed to identify potential hazards related to the complaint.

### 5. AI Confidence Score
The system displays an AI confidence score representing how certain the model is about the predicted priority.

---

## Technologies Used

Backend:
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Bcrypt

Machine Learning:
- Scikit-learn
- TF-IDF Vectorization
- Random Forest Classifier
- Cosine Similarity

Frontend:
- HTML
- CSS
- JavaScript
- Jinja2 Templates

Database:
- SQLite

Deployment:
- Render Cloud Platform
- Gunicorn Web Server

---

## System Architecture

User → Submit Complaint  
↓  
AI Model Processes Complaint Description  
↓  
Priority Prediction + Risk Classification  
↓  
Complaint Stored in Database  
↓  
Admin Dashboard for Monitoring & Resolution  

---

## Demo Credentials

### Admin

Username: `admin@test.com`  
Password: `admin123`

### User

Username: `user@test.com`  
Password: `user123`

---

## Demo Notice

This project is deployed on Render's free hosting tier for demonstration purposes.

Due to the use of ephemeral storage, the database may reset after periods of inactivity or service restarts.

If the system appears empty, please submit a few sample complaints to explore the platform features.

Recommended: Submit at least **3 complaints** to view the analytics and AI prioritization working effectively.

---

## Example Complaints for Testing

1. Large pothole on highway causing accidents  
2. Garbage not collected in residential area for several days  
3. Broken streetlight near school causing safety issues  
4. Water leakage from damaged pipeline  
5. Open sewage drain causing health hazards

---

## Project Goal

The goal of this project is to demonstrate how artificial intelligence can support smart-city governance by helping authorities automatically prioritize civic issues and respond more efficiently to public grievances.

---

## Author

Vadla Varshith Raj  
B.Tech Computer Science and Engineering  
CMR Technical Campus, Hyderabad

---

## Research Focus

This project is part of research work on:

**AI Trained Civic Grievance Prioritization System for Smart Urban Management**

The system explores the use of machine learning and natural language processing for intelligent urban governance systems.
---
## System Screenshots

### Login Interface
![Login](screenshots/login.png)

### User Dashboard
![Dashboard](screenshots/user_dashboard.png)

### AI Complaint Analysis
![AI Analysis](screenshots/ai_prediction.png)

### Admin Dashboard
![Admin Dashboard](screenshots/admin_dashboard.png)
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

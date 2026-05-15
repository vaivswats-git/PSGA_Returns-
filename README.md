# Personal Skill Gap Analyzer Returns

## Overview
Personal Skill Gap Analyzer Returns is an AI-powered career guidance and skill development platform designed to help users identify suitable career paths based on their skills, analyze missing competencies, access personalized learning resources, practice through mock tests, and follow structured career roadmaps.

---

## Features

### User Authentication
- Secure Signup/Login
- User profile management
- Personalized dashboard access

### Career Prediction
- Random Forest Machine Learning model
- Skill-based career recommendations
- Career match analysis

### Skill Gap Analysis
- Compares user skills with career requirements
- Identifies missing skills
- Suggests improvement areas

### Company Recommendations
- Career-specific company suggestions
- Multiple company options for each domain

### Learning Resources
- Free clickable course links
- Skill-specific recommendations
- Multi-domain course coverage

### Mock Tests
- API-powered dynamic quizzes
- Local backup question bank
- Randomized assessments
- Score tracking

### Career Roadmaps
- Step-by-step growth paths
- Personalized development guidance

### Progress Tracking
- Course completion tracking
- Mock test score history
- Skill development monitoring

### Streak System
- Daily activity streaks
- User consistency tracking

---

## Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Requests API
- JSON

---

## Project Structure
```txt
PersonalSkillGapAnalyzer_Returns/

├── app.py
├── requirements.txt
├── README.md

├── data/
│   ├── jobs.json
│   ├── companies.json
│   ├── courses.json
│   ├── roadmaps.json
│   ├── mock_tests.json
│   ├── users.json
│   ├── progress_data.json
│   └── streak_data.json

├── modules/
│   ├── auth.py
│   ├── dashboard.py
│   ├── career.py
│   ├── learning_resources.py
│   ├── mock_test.py
│   ├── roadmap.py
│   ├── progress.py
│   └── streak.py

├── api/
│   └── api_handler.py

└── models/
    ├── career_model.pkl
    ├── skill_encoder.pkl
    ├── label_encoder.pkl
    └── train_model.py
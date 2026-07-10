# 🎓 AI-Based Student Placement Prediction System

## 📌 Project Overview

The **AI-Based Student Placement Prediction System** is a Machine Learning web application developed using **Python** and **Streamlit**. It predicts whether a student is likely to be placed based on academic and skill-related factors such as CGPA, internship experience, projects, communication skills, technical skills, aptitude score, and certifications.

The system also provides career improvement suggestions, company eligibility recommendations, resume analysis, prediction reports in PDF format, email notifications, analytics dashboards, and batch prediction using CSV/Excel files.

---

# 🚀 Features

### 👨‍🎓 Student Features
- Student Placement Prediction
- Resume Upload & Analysis (PDF)
- Resume Score Generation
- Prediction Confidence Score
- Career Improvement Suggestions
- Company Eligibility Recommendations
- Download Prediction Report (PDF)
- Email Notification with PDF Report
- Multiple Machine Learning Model Selection

### 👨‍💼 Admin Features
- View Prediction History
- Search Student Records
- Delete Prediction Records
- Download Prediction History (CSV)

### 📊 Analytics Features
- Placement Statistics Dashboard
- Pie Chart Visualization
- Prediction History Analysis
- Model Performance Metrics
  - Accuracy
  - Precision
  - Recall
  - F1-Score

### 📂 Batch Prediction
- Upload CSV Dataset
- Upload Excel Dataset
- Predict Placement for Multiple Students
- Download Prediction Results

---

# 🧠 Machine Learning Models Used

- Random Forest Classifier
- Decision Tree Classifier
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

---

# 🛠 Technologies Used

### Programming Language
- Python 3.x

### Libraries
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- ReportLab
- PyPDF2
- pdfplumber
- yagmail
- mysql-connector-python

### Database
- MySQL

### Development Environment
- Visual Studio Code
- MySQL Workbench

---

# 📂 Project Structure

```text
placement prediction system/
│
├── app.py
├── database.py
├── email_sender.py
├── reports.py
├── resume_analyzer.py
├── admin.py
├── analysis.py
├── performance.py
├── requirements.txt
├── README.md
│
├── data/
│   └── placement.csv
│
├── models/
│   ├── random_forest.pkl
│   ├── decision_tree.pkl
│   ├── logistic_regression.pkl
│   ├── knn.pkl
│   └── svm.pkl
│
├── reports/
│
├── .streamlit/
│   └── secrets.toml
│
└── screenshots/
```

---

# ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/placement-prediction-system.git
```

### Navigate to the project

```bash
cd placement-prediction-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL

Create a database:

```sql
CREATE DATABASE placement_ai;
```

Update the database credentials in `database.py`.

### Configure Email

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
EMAIL = "yourgmail@gmail.com"
PASSWORD = "your_google_app_password"
```

### Run the application

```bash
streamlit run app.py
```

---

# 📊 Model Performance

The application displays the following evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-Score

These metrics help compare the performance of different machine learning models.

---

# 📈 Dashboard

The Analytics Dashboard provides:

- Total Predictions
- Placed Students
- Not Placed Students
- Placement Percentage
- Pie Chart Visualization
- Prediction History

---

# 📧 Email Notification

After a prediction is generated:

- A PDF report is created.
- The report can be downloaded.
- The report can also be emailed directly to the student's email address.

---

# 📄 PDF Report

Each report contains:

- Student Name
- Selected Machine Learning Model
- Prediction Result
- Prediction Confidence
- Generated Date

---

# 📂 Batch Prediction

The application supports bulk predictions by uploading:

- CSV files
- Excel (.xlsx) files

The output includes:

- Prediction
- Probability (%)

Users can download the results as a CSV file.

---

# 📸 Screenshots

Add screenshots of the following pages:

- Home Page
- Prediction Page
- Resume Analysis
- Analytics Dashboard
- Data Analysis
- Model Performance
- Batch Prediction
- Admin Dashboard

---

# 📌 Limitations

- Predictions depend on the quality of the training dataset.
- Resume analysis is keyword-based and not full NLP.
- Company recommendations are rule-based.
- Email notifications require Gmail App Password configuration.
- The system is intended for educational purposes.

---

# 🚀 Future Enhancements

- Deep Learning-based prediction models
- AI-powered Resume Analysis using NLP
- Interview Preparation Chatbot
- LinkedIn Profile Analysis
- Live Company Recruitment API Integration
- Student Login Authentication
- Mobile Application
- Cloud Database Integration

---

# 👨‍💻 Developed By

ANUSHIKA
BCA-III
7031/24
PGGC-11
Panjab University

Python & AI Internship Project

---

# 📜 License

This project is developed for educational and learning purposes.
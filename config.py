# ==========================================
# AI Placement Prediction System - Config
# ==========================================

APP_TITLE = "🎓 AI-Based Student Placement Prediction System"
APP_ICON = "🎓"
LAYOUT = "wide"

# -------------------------------
# MySQL Configuration
# -------------------------------

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Root123"      # Change if your MySQL password is different
DB_NAME = "placement_ai"

# -------------------------------
# Machine Learning Models
# -------------------------------

MODEL_FILES = {
    "Random Forest": "models/random_forest.pkl",
    "Decision Tree": "models/decision_tree.pkl",
    "Logistic Regression": "models/logistic_regression.pkl",
    "KNN": "models/knn.pkl",
    "SVM": "models/svm.pkl"
}

# -------------------------------
# Dataset
# -------------------------------

DATASET = "data/placement.csv"

MODEL_RESULTS = "models/model_results.csv"
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from users.login import login
from database import get_connection, save_prediction
from users.admin import admin_dashboard
from reports.pdf_report import create_pdf
from resume.resume_analyzer import analyze_resume
from email_sender import send_email
from email_sender import send_email
# PAGE SETTINGS
st.set_page_config(
    page_title="AI Placement Prediction System",
    page_icon="🎓",
    layout="wide"
)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""
# CUSTOM CSS
st.markdown("""
<style>
/* Make all text white */
h1, h2, h3, h4, h5, h6,
p,
label,
span,
div,
li {
    color: white !important;
}

/* Metric labels and values */
[data-testid="metric-container"] label,
[data-testid="metric-container"] div {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)
# LOAD MODEL & DATA
model = joblib.load("models/placement_model.pkl")
df = pd.read_csv("data/placement.csv")
results = pd.read_csv("models/model_results.csv")
if not st.session_state.logged_in:
    login()
    st.stop()
# SIDEBAR
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home",
        "📊 Data Analysis",
        "⭐ Prediction",
        "📈 Model Comparison",
        "📊 Model Performance",
        "👨‍💼 Admin Dashboard",
        "📈 Analytics Dashboard",
        "📂 Batch Prediction",
        "✨ About"
    ]
)
st.sidebar.divider()

if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.role = ""

    st.rerun()
# HOME PAGE
if page == "🏠 Home":

    st.markdown("""
<h1 style='text-align:center;
color:#1E3A8A;'>
🎓 AI-Based Student Placement Prediction System
</h1>
""", unsafe_allow_html=True)

    st.markdown(
        "<h4 style='text-align:center;color:#475569;'>Python + AI Internship Project</h4>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("""
<p style="color:#334155; font-size:20px;">
Welcome to the **AI-Based Student Placement Prediction System**.

This project predicts whether a student is likely to be placed based on:

- 📚 CGPA
- 💼 Internship
- 📁 Projects
- 🗣 Communication Skills
- 💻 Technical Skills
- 🧠 Aptitude Score
- 📜 Certifications
"""
, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Students", len(df))


    with col2:
        st.metric(
            "Placed",
            len(df[df["Placement"] == "Yes"])
        )

    with col3:
        st.metric(
            "Not Placed",
            len(df[df["Placement"] == "No"])
        )

    st.info("👈 Use the sidebar to navigate through the project.")
# DATA ANALYSIS
elif page == "📊 Data Analysis":

    st.title("📊 Data Analysis Dashboard")

    st.markdown("""
<h3 style="color:#1D4ED8;">
📊 Dataset Preview
</h3>
""", unsafe_allow_html=True)

    st.dataframe(df)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Placement Distribution")

        fig, ax = plt.subplots(figsize=(5,4))

        sns.countplot(
            data=df,
            x="Placement",
            ax=ax
        )

        st.pyplot(fig)

    with col2:

        st.subheader("Average CGPA by Placement")

        fig2, ax2 = plt.subplots(figsize=(5,4))

        sns.barplot(
            data=df,
            x="Placement",
            y="CGPA",
            ax=ax2
        )

        st.pyplot(fig2)

    st.divider()

    st.subheader("Placement Percentage")

    fig3, ax3 = plt.subplots(figsize=(5,5))

    placement = df["Placement"].value_counts()

    ax3.pie(
        placement,
        labels=placement.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax3.axis("equal")

    st.pyplot(fig3)

    st.divider()

    st.subheader("Dataset Statistics")

    st.write(df.describe())
# PREDICTION
# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "⭐ Prediction":

    st.title("⭐ Placement Prediction")

    # -----------------------------
    # Student Details
    # -----------------------------

    student_name = st.text_input(
        "👤 Student Name"
    )
    email = st.text_input(
    "📧 Enter Email Address"
)


    selected_model = st.selectbox(
        "Choose Machine Learning Model",
        [
            "Random Forest",
            "Decision Tree",
            "Logistic Regression",
            "KNN",
            "SVM"
        ]
    )

    model_files = {
        "Random Forest": "models/random_forest.pkl",
        "Decision Tree": "models/decision_tree.pkl",
        "Logistic Regression": "models/logistic_regression.pkl",
        "KNN": "models/knn.pkl",
        "SVM": "models/svm.pkl"
    }

    model = joblib.load(
        model_files[selected_model]
    )

    st.divider()

    col1, col2 = st.columns(2)

    # -----------------------------
    # LEFT COLUMN
    # -----------------------------

    with col1:

        cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            value=7.0,
            step=0.1
        )

        internship = st.selectbox(
            "Internship",
            [
                "Yes",
                "No"
            ]
        )

        projects = st.number_input(
            "Projects Completed",
            min_value=0,
            max_value=10,
            value=2
        )

        aptitude = st.number_input(
            "Aptitude Score",
            min_value=0,
            max_value=100,
            value=70
        )

    # -----------------------------
    # RIGHT COLUMN
    # -----------------------------

    with col2:

        communication = st.slider(
            "Communication Skills",
            1,
            10,
            7
        )

        technical = st.slider(
            "Technical Skills",
            1,
            10,
            7
        )

        certifications = st.number_input(
            "Certifications",
            min_value=0,
            max_value=10,
            value=1
        )

    internship = 1 if internship == "Yes" else 0

    st.divider()

    # -----------------------------
    # Resume Upload
    # -----------------------------

    st.subheader("📄 Resume Analysis")
    uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"],
    key="resume_upload"
)

    st.divider()
    if st.button("🚀 Predict Placement"):
                # ---------------------------------
        # Resume Analysis
        # ---------------------------------

        if uploaded_resume is not None:

            score, skills = analyze_resume(uploaded_resume)

            st.success(f"📊 Resume Score: {score}/100")

            st.write("### Skills Found")

            st.write(skills)

            if score < 50:
                st.warning(
                    "💡 Improve your resume by adding more technical skills, projects and certifications."
                )

        else:

            score = 0
            skills = []

        # ---------------------------------
        # Prepare Input
        # ---------------------------------

        input_data = np.array([[
            cgpa,
            internship,
            projects,
            communication,
            technical,
            aptitude,
            certifications
        ]])

        # ---------------------------------
        # Prediction
        # ---------------------------------

        prediction = model.predict(input_data)

        probability = model.predict_proba(input_data)[0][1]

        result = "Placed" if prediction[0] == 1 else "Not Placed"

        # ---------------------------------
        # Display Result
        # ---------------------------------

        if prediction[0] == 1:

            st.balloons()

            st.success("🎉 Student is Likely to be PLACED")

        else:

            st.error("❌ Student is NOT Likely to be Placed")

        st.metric(
            "Prediction Confidence",
            f"{probability*100:.2f}%"
        )

        st.progress(float(probability))

        # ---------------------------------
        # Career Suggestions
        # ---------------------------------

        if prediction[0] == 0:

            st.divider()

            st.subheader("📈 Career Improvement Suggestions")

            suggestions = []

            if cgpa < 7:
                suggestions.append("📚 Improve your CGPA to above 7.5.")

            if internship == 0:
                suggestions.append("💼 Complete at least one internship.")

            if projects < 3:
                suggestions.append("📁 Build more real-world projects.")

            if communication < 7:
                suggestions.append("🗣 Improve your communication skills.")

            if technical < 7:
                suggestions.append("💻 Improve your programming skills.")

            if certifications < 2:
                suggestions.append("📜 Complete online certifications.")

            if aptitude < 70:
                suggestions.append("🧠 Practice aptitude and logical reasoning.")

            if len(suggestions) == 0:
                st.success("Excellent profile! Keep improving.")

            else:
                for tip in suggestions:
                    st.info(tip)
                            # ---------------------------------
        # Company Eligibility Recommendation
        # ---------------------------------

        st.divider()

        st.subheader("🏢 Company Eligibility Recommendations")

        companies = []

        if prediction[0] == 1:

            if (
                cgpa >= 9.0 and
                technical >= 9 and
                communication >= 8 and
                aptitude >= 90
            ):

                companies = [
                    ("Google", "₹30-60 LPA"),
                    ("Microsoft", "₹25-50 LPA"),
                    ("Amazon", "₹20-45 LPA"),
                    ("Adobe", "₹18-40 LPA"),
                    ("Oracle", "₹12-25 LPA")
                ]

            elif (
                cgpa >= 8.5 and
                technical >= 8 and
                aptitude >= 85
            ):

                companies = [
                    ("IBM", "₹8-18 LPA"),
                    ("Deloitte", "₹7-15 LPA"),
                    ("Cisco", "₹10-22 LPA"),
                    ("Accenture", "₹6-12 LPA"),
                    ("Infosys", "₹5-10 LPA")
                ]

            elif (
                cgpa >= 7.5 and
                technical >= 7
            ):

                companies = [
                    ("TCS", "₹3.5-9 LPA"),
                    ("Infosys", "₹3.6-9 LPA"),
                    ("Wipro", "₹3.5-8 LPA"),
                    ("Capgemini", "₹4-8 LPA"),
                    ("Cognizant", "₹4-9 LPA"),
                    ("HCL Technologies", "₹4-8 LPA")
                ]

            else:

                companies = [
                    ("Local IT Companies", "₹2-5 LPA"),
                    ("Startups", "₹3-8 LPA"),
                    ("Internships", "Stipend Based")
                ]

            company_df = pd.DataFrame(
                companies,
                columns=["Company", "Expected Package"]
            )

            st.dataframe(
                company_df,
                use_container_width=True
            )

        else:

            st.warning(
                "Improve your profile before applying to top companies."
            )

        st.info(
            "📌 Company recommendations are indicative only. Actual hiring criteria vary by company and recruitment cycle."
        )

        # ---------------------------------
        # Save Prediction
        # ---------------------------------

        save_prediction(
            student_name,
            result,
            float(probability),
            selected_model
        )

        st.success("✅ Prediction saved to MySQL database.")

        # Generate PDF Report
        pdf_file = create_pdf(
            student_name,
            result,
            probability * 100,
            selected_model
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )

        # Send Email
        if email:

            try:

                send_email(
                    email,
                    student_name,
                    pdf_file
                )

                st.success("📧 Prediction Report Sent Successfully!")

            except Exception as e:

                st.error(f"Email Error:\n{e}")

        # =====================================================
# MODEL COMPARISON
# =====================================================

elif page == "📈 Model Comparison":

    st.title("📈 Machine Learning Model Comparison")

    st.success("Performance of all trained Machine Learning models")

    st.dataframe(results, use_container_width=True)

    st.divider()

    st.subheader("Accuracy Comparison")

    fig, ax = plt.subplots(figsize=(8,4))

    sns.barplot(
        data=results,
        x="Model",
        y="Accuracy",
        ax=ax
    )

    plt.xticks(rotation=15)

    st.pyplot(fig)

    st.divider()

    st.subheader("Precision, Recall & F1 Score")

    st.dataframe(results.style.highlight_max(axis=0))
    selected_model = st.selectbox(
        "Choose Machine Learning Model",
    [
        "Random Forest",
        "Decision Tree",
        "Logistic Regression",
        "KNN",
        "SVM"
    ]
)
    model_files = {
        "Random Forest": "models/random_forest.pkl",
        "Decision Tree": "models/decision_tree.pkl",
        "Logistic Regression": "models/logistic_regression.pkl",
        "KNN": "models/knn.pkl",
        "SVM": "models/svm.pkl"
        }
    model = joblib.load(model_files[selected_model])
elif page == "👨‍💼 Admin Dashboard":

    if st.session_state.role != "Admin":

        st.error("Only Admin can access this page.")

    else:

        admin_dashboard()
elif page == "📊 Model Performance":

    st.title("📊 Machine Learning Model Performance")

    results = pd.read_csv("models/model_results.csv")

    st.dataframe(
        results,
        use_container_width=True
    )

    st.divider()

    st.subheader("Accuracy Comparison")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        results["Model"],
        results["Accuracy"]
    )

    ax.set_ylabel("Accuracy")

    st.pyplot(fig)

    st.divider()

    st.subheader("Performance Metrics")

    st.line_chart(
        results.set_index("Model")
    )
        # =====================================================
# ANALYTICS DASHBOARD
# =====================================================

elif page == "📈 Analytics Dashboard":

    st.title("📈 Placement Analytics Dashboard")
    conn = get_connection()

    query = """
    SELECT * FROM prediction_history
    """

    history = pd.read_sql(query, conn)

    conn.close()

    if history.empty:
        st.warning("No prediction history available.")
    else:

        # -------------------------
        # Metrics
        # -------------------------

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Predictions", len(history))

        col2.metric(
            "Placed",
            len(history[history["prediction"] == "Placed"])
        )

        col3.metric(
            "Not Placed",
            len(history[history["prediction"] == "Not Placed"])
        )

        col4.metric(
            "Average Probability",
            f"{history['probability'].mean():.2f}%"
        )

        st.divider()

        # -------------------------
        # Pie Chart
        # -------------------------

        st.subheader("🥧 Placement Distribution")

        fig1, ax1 = plt.subplots(figsize=(5,5))

        placement = history["prediction"].value_counts()

        ax1.pie(
            placement,
            labels=placement.index,
            autopct="%1.1f%%",
            startangle=90
        )

        ax1.axis("equal")

        st.pyplot(fig1)

        st.divider()

        # -------------------------
        # Model Usage
        # -------------------------

        st.subheader("🤖 Model Usage")

        fig2, ax2 = plt.subplots(figsize=(7,4))

        history["model_used"].value_counts().plot(
            kind="bar",
            ax=ax2
        )

        ax2.set_xlabel("Model")

        ax2.set_ylabel("Predictions")

        st.pyplot(fig2)

        st.divider()

        # -------------------------
        # Prediction Confidence
        # -------------------------

        st.subheader("📊 Prediction Confidence")

        fig3, ax3 = plt.subplots(figsize=(7,4))

        history["probability"].hist(
            bins=10,
            ax=ax3
        )

        ax3.set_xlabel("Probability (%)")

        st.pyplot(fig3)

        st.divider()

        # -------------------------
        # Table
        # -------------------------

        st.subheader("Prediction History")

        st.dataframe(
            history,
            use_container_width=True
        )
        # =====================================================
# BATCH PREDICTION
# =====================================================
elif page == "📂 Batch Prediction":

    st.title("📂 Batch Prediction using CSV / Excel")

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv", "xlsx"],
        key="dataset_upload"
    )

    if uploaded_file is not None:

        # Read file
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)

        # Rename columns
        data.columns = data.columns.str.strip()

        data.rename(columns={
            "INTERNSHIP": "Internship",
            "PROJECTS": "Projects",
            "COMMUNICATION": "Communication",
            "TECHNICAL": "Technical",
            "APTITUDE": "Aptitude",
            "CERTIFICATIONS": "Certifications"
        }, inplace=True)

        st.subheader("Dataset Preview")
        st.dataframe(data)

        required_columns = [
            "CGPA",
            "Internship",
            "Projects",
            "Communication",
            "Technical",
            "Aptitude",
            "Certifications"
        ]

        if all(col in data.columns for col in required_columns):

            data["Internship"] = (
                data["Internship"]
                .astype(str)
                .str.upper()
                .map({
                    "YES": 1,
                    "NO": 0
                })
            )

            X = data[required_columns]

            # Load default model
            batch_model = joblib.load("models/random_forest.pkl")

            predictions = batch_model.predict(X)

            probabilities = batch_model.predict_proba(X)[:, 1]

            data["Prediction"] = [
                "Placed" if p == 1 else "Not Placed"
                for p in predictions
            ]

            data["Probability (%)"] = (probabilities * 100).round(2)

            st.success("Prediction Completed Successfully!")

            st.dataframe(data)

            st.download_button(
                "📥 Download Prediction Results",
                data.to_csv(index=False),
                file_name="batch_prediction_results.csv",
                mime="text/csv"
            )

        else:

            st.error("Dataset does not contain the required columns.")

            st.write(required_columns)
# =====================================================
# ABOUT
# =====================================================

elif page == "✨ About":

    st.title("✨ About Project")

    st.success("BCA (NEP) | Python + AI Internship Project")

    st.markdown("""
### 👨‍💻 Technologies Used

- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 📈 Seaborn
- 🤖 Scikit-learn
- 🌐 Streamlit

### 🧠 Machine Learning Algorithm

**Random Forest Classifier**

### 🎯 Project Objective

Predict whether a student is likely to be placed using academic performance and skill-based features.

### 🏫 University

**Panjab University**

### 📚 Course

**Bachelor of Computer Applications (BCA - NEP)**

### 💡 Internship

**Python + AI**
""")

    st.divider()

    st.caption("Developed as part of the Python + AI Internship Project")
import streamlit as st
import yagmail
def send_email(receiver_email, student_name, pdf_file):
    sender_email = st.secrets["EMAIL"]
    app_password = st.secrets["PASSWORD"]

    yag = yagmail.SMTP(
        sender_email,
        app_password
    )

    subject = "Placement Prediction Report"

    body = f"""
Hello {student_name},

Your AI Placement Prediction Report is attached.

Thank you for using the AI Placement Prediction System.

Regards,
Placement Prediction Team
"""

    yag.send(
        to=receiver_email,
        subject=subject,
        contents=body,
        attachments=pdf_file
    )
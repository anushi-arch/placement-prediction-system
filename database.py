import mysql.connector
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["DB_HOST"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        database=st.secrets["DB_NAME"],
        port=int(st.secrets["DB_PORT"])
    )
def save_prediction(student_name, prediction, probability, model_used):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO prediction_history
    (student_name, prediction, probability, model_used)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        student_name,
        prediction,
        probability,
        model_used
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
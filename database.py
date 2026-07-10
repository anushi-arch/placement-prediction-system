import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="placement_ai"
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
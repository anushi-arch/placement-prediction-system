import streamlit as st
import pandas as pd
from database import get_connection
import matplotlib.pyplot as plt
def admin_dashboard():

    st.title("ADMIN DASHBOARD")

    conn = get_connection()

    query = """
    SELECT * FROM prediction_history
    ORDER BY prediction_date DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    if df.empty:
        st.warning("No prediction history found.")
        return

    # Statistics
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Predictions", len(df))

    col2.metric(
        "Placed",
        len(df[df["prediction"] == "Placed"])
    )

    col3.metric(
        "Not Placed",
        len(df[df["prediction"] == "Not Placed"])
    )
    placement = df["prediction"].value_counts()
    fig, ax = plt.subplots(figsize=(5,5))
    ax.pie(
    placement,
    labels=placement.index,
    autopct="%1.1f%%",
    startangle=90
)

    ax.axis("equal")

    st.pyplot(fig)
    st.divider()

    # Search
    search = st.text_input("🔍 Search Student")

    if search:

        df = df[
            df["student_name"].str.contains(
                search,
                case=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True
    )
    st.download_button(
        label="Download Prediction History (CSV)",
        data=df.to_csv(index=False),
        file_name="prediction_history.csv",
        mime="text/csv"
    )
    st.divider()

    st.subheader("Delete Prediction Record")

    record_id = st.number_input(
        "Enter Record ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Record"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM prediction_history WHERE id=%s",
            (record_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

        st.success("Record Deleted Successfully!")

        st.rerun()
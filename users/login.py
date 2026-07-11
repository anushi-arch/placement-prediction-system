import streamlit as st

def login():

    st.title("LOGIN")

    user_type = st.selectbox(
        "Login As",
        ["Student", "Admin"]
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if user_type == "Admin":

            if username == "admin" and password == "admin123":

                st.session_state.logged_in = True
                st.session_state.role = "Admin"

                st.success("Admin Login Successful")

            else:
                st.error("Invalid Admin Credentials")

        else:
            if (
                username == st.secrets["STUDENT_USERNAME"]
                and password == st.secrets["STUDENT_PASSWORD"]
                ):

                st.session_state.logged_in = True
                st.session_state.role = "Student"

                st.success("Student Login Successful")

            else:
                st.error("Invalid Student Credentials")
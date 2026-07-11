import streamlit as st

def login():

    st.title("PLACEMENT PREDICTION SYSTEM")

    st.subheader("Choose Access")

    col1, col2 = st.columns(2)

    # -------------------------
    # Student Access
    # -------------------------
    with col1:

        st.info("Student")

        st.write("Continue without login.")

        if st.button("Continue as Student"):

            st.session_state.logged_in = True
            st.session_state.role = "Student"

            st.rerun()

    # -------------------------
    # Admin Login
    # -------------------------
    with col2:

        st.info("Admin")

        username = st.text_input(
            "Admin Username"
        )

        password = st.text_input(
            "Admin Password",
            type="password"
        )

        if st.button("Admin Login"):

            if (
                username == st.secrets["ADMIN_USERNAME"]
                and
                password == st.secrets["ADMIN_PASSWORD"]
            ):

                st.session_state.logged_in = True
                st.session_state.role = "Admin"

                st.success("Admin Login Successful")
                st.rerun()

            else:

                st.error("Invalid Admin Credentials")
import streamlit as st
from auth import login, register


def show_login():

    st.title("🎓 StudyAI")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # LOGIN
    with tab1:

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            if login(username, password):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid Username or Password")

    # REGISTER
    with tab2:

        new_user = st.text_input(
            "Create Username",
            key="register_user"
        )

        new_pass = st.text_input(
            "Create Password",
            type="password",
            key="register_pass"
        )

        if st.button("Register"):

            success, message = register(
                new_user,
                new_pass
            )

            if success:
                st.success(message)
            else:
                st.error(message)
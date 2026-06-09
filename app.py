import streamlit as st

from database import create_tables

from roadmap import show_roadmaps
from quiz import show_quiz
from leaderboard import show_leaderboard
from planner import show_planner
from dashboard import show_dashboard
from notes import show_notes
from analytics import show_analytics
from ai_tutor import show_ai_tutor
from login_page import show_login

create_tables()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    show_login()
    st.stop()

username = st.session_state.username

st.sidebar.title("StudyAI")
st.sidebar.write(
    f"👤 {username}"
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    if "username" in st.session_state:
        del st.session_state["username"]

    st.rerun()

page = st.sidebar.radio(
    "Navigation",
    [
    "Dashboard",
    "Roadmaps",
    "Quiz",
    "Planner",
    "Leaderboard",
    "Notes",
    "Analytics",
    "AI Tutor"
    ]
)

if page == "Dashboard":
    show_dashboard(username)

elif page == "Roadmaps":
    show_roadmaps()

elif page == "Quiz":
    show_quiz(username)

elif page == "Planner":
    show_planner(username)

elif page == "Leaderboard":
    show_leaderboard()

elif page == "Notes":
    show_notes()

elif page == "Analytics":
    show_analytics(username)

elif page == "AI Tutor":
    show_ai_tutor()
import streamlit as st

from database import (
    get_user_info,
    calculate_level
)


def show_dashboard(username):

    user = get_user_info(username)

    if not user:
        st.error("User not found")
        return

    xp = user[1]

    level = calculate_level(xp)

    st.title("🎓 Student Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Username",
            username
        )

    with col2:
        st.metric(
            "XP",
            xp
        )

    with col3:
        st.metric(
            "Level",
            level
        )

    progress = min(
        xp / 2500,
        1.0
    )

    st.subheader(
        "Level Progress"
    )

    st.progress(progress)

    st.write(
        f"{round(progress*100)}% to Master"
    )
import streamlit as st
import pandas as pd
from database import get_leaderboard


def show_leaderboard():

    st.title("🏆 Global Leaderboard")

    data = get_leaderboard()

    if not data:
        st.warning("No users found.")
        return

    df = pd.DataFrame(
        data,
        columns=["Username", "XP"]
    )

    df.index = df.index + 1

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success(
        f"Top Student: {df.iloc[0]['Username']}"
    )
import streamlit as st
import pandas as pd
import plotly.express as px

from database import get_user_results


def show_analytics(username):

    st.title("📊 Performance Analytics")

    results = get_user_results(username)

    if not results:
        st.warning(
            "No quiz data available."
        )
        return

    data = []

    for row in results:

        data.append({
            "Subject": row[2],
            "Score": row[3]
        })

    df = pd.DataFrame(data)

    st.subheader(
        "Quiz Results"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        "Subject Performance"
    )

    fig = px.bar(
        df,
        x="Subject",
        y="Score",
        title="Scores by Subject"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    average = round(
        df["Score"].mean(),
        2
    )

    highest = df["Score"].max()

    lowest = df["Score"].min()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average",
            average
        )

    with col2:
        st.metric(
            "Highest",
            highest
        )

    with col3:
        st.metric(
            "Lowest",
            lowest
        )
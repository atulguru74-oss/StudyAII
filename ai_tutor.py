import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

import streamlit as st
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def initialize_chat():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def ask_ai(question):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are StudyAI.

Rules:
- Help students learn.
- Explain step by step.
- Generate quizzes when requested.
- Create study roadmaps.
- Solve math problems clearly.
- Be friendly and educational.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

def show_ai_tutor():

    st.title("🤖 StudyAI Tutor")

    initialize_chat()

    question = st.text_area(
        "Ask any question",
        height=120
    )

    if st.button("Ask AI"):

        if question.strip():

            answer = ask_ai(question)

            st.session_state.chat_history.append(
                ("You", question)
            )

            st.session_state.chat_history.append(
                ("StudyAI", answer)
            )

    for role, text in st.session_state.chat_history:

        if role == "You":
            st.markdown(f"**👨‍🎓 {role}:** {text}")
        else:
            st.markdown(f"**🤖 {role}:** {text}")
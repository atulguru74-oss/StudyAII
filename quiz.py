import random
import streamlit as st
from database import save_quiz_result, update_xp


QUIZZES = {
    "Mathematics": [
        {
            "question": "What is 12 × 12?",
            "options": ["124", "144", "132", "142"],
            "answer": "144",
            "explanation": "12 multiplied by 12 equals 144."
        },

        {
            "question": "Square root of 81?",
            "options": ["7", "8", "9", "10"],
            "answer": "9",
            "explanation": "9 × 9 = 81."
        }
    ],

    "Physics": [
        {
            "question": "SI unit of force?",
            "options": ["Joule", "Newton", "Pascal", "Volt"],
            "answer": "Newton",
            "explanation": "Force is measured in Newtons."
        }
    ],

    "Chemistry": [
        {
            "question": "Chemical formula of water?",
            "options": ["CO2", "O2", "H2O", "NaCl"],
            "answer": "H2O",
            "explanation": "Water contains two hydrogen atoms and one oxygen atom."
        }
    ]
}


def show_quiz(username):

    st.title("📝 Practice Quiz")

    subject = st.selectbox(
        "Select Subject",
        list(QUIZZES.keys())
    )

    questions = QUIZZES[subject]

    score = 0

    user_answers = []

    for index, q in enumerate(questions):

        answer = st.radio(
            q["question"],
            q["options"],
            key=f"quiz_{index}"
        )

        user_answers.append(answer)

    if st.button("Submit Quiz"):

        st.subheader("Results")

        for i, q in enumerate(questions):

            if user_answers[i] == q["answer"]:
                score += 1
                st.success(
                    f"✅ {q['question']}"
                )

            else:
                st.error(
                    f"❌ {q['question']}"
                )

            st.info(
                f"Explanation: {q['explanation']}"
            )

        total = len(questions)

        percentage = int(
            (score / total) * 100
        )

        st.metric(
            "Score",
            f"{score}/{total}"
        )

        st.metric(
            "Percentage",
            f"{percentage}%"
        )

        earned_xp = score * 10

        update_xp(
            username,
            earned_xp
        )

        save_quiz_result(
            username,
            subject,
            percentage
        )

        st.success(
            f"You earned {earned_xp} XP!"
        )
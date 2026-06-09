import streamlit as st
from database import get_connection


def add_task(username, task):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO study_plans(
        username,
        task,
        completed
        )
        VALUES(?,?,0)
        """,
        (username, task)
    )

    conn.commit()
    conn.close()


def get_tasks(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,task,completed
        FROM study_plans
        WHERE username=?
        """,
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data


def update_task(task_id, completed):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE study_plans
        SET completed=?
        WHERE id=?
        """,
        (completed, task_id)
    )

    conn.commit()
    conn.close()


def delete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM study_plans
        WHERE id=?
        """,
        (task_id,)
    )

    conn.commit()
    conn.close()


def show_planner(username):

    st.title("📅 Study Planner")

    task = st.text_input(
        "Add Study Goal"
    )

    if st.button("Add Goal"):

        if task.strip():
            add_task(
                username,
                task
            )
            st.rerun()

    st.subheader("My Goals")

    tasks = get_tasks(username)

    if not tasks:
        st.info(
            "No study goals added."
        )

    for task_id, task_name, completed in tasks:

        col1, col2 = st.columns([5, 1])

        with col1:

            checked = st.checkbox(
                task_name,
                value=bool(completed),
                key=f"task_{task_id}"
            )

            if checked != bool(completed):

                update_task(
                    task_id,
                    int(checked)
                )

        with col2:

            if st.button(
                "❌",
                key=f"delete_{task_id}"
            ):
                delete_task(task_id)
                st.rerun()
import streamlit as st

ROADMAPS = {
    "Mathematics": [
        "Number System",
        "Algebra",
        "Linear Equations",
        "Quadratic Equations",
        "Coordinate Geometry",
        "Trigonometry",
        "Statistics",
        "Probability"
    ],

    "Physics": [
        "Motion",
        "Force",
        "Work & Energy",
        "Gravitation",
        "Waves",
        "Electricity",
        "Magnetism",
        "Modern Physics"
    ],

    "Chemistry": [
        "Atoms & Molecules",
        "Periodic Table",
        "Chemical Bonding",
        "Acids & Bases",
        "Organic Chemistry",
        "Hydrocarbons",
        "Polymers",
        "Biochemistry"
    ],

    "Biology": [
        "Cell Biology",
        "Genetics",
        "Human Body",
        "Evolution",
        "Ecology",
        "Plant Physiology",
        "Microbiology",
        "Biotechnology"
    ]
}


def show_roadmaps():
    st.title("📚 Subject Roadmaps")

    subject = st.selectbox(
        "Choose Subject",
        list(ROADMAPS.keys())
    )

    topics = ROADMAPS[subject]

    completed = 0

    for topic in topics:
        done = st.checkbox(topic, key=f"{subject}_{topic}")

        if done:
            completed += 1

    progress = completed / len(topics)

    st.progress(progress)

    st.write(
        f"Progress: {int(progress * 100)}%"
    )

    if progress == 1:
        st.success("🎉 Roadmap Completed!")
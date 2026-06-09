import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(title, content, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = [
        Paragraph(title, styles["Title"]),
        Spacer(1, 12),
        Paragraph(content.replace("\n", "<br/>"), styles["BodyText"])
    ]

    doc.build(elements)

    return filename


def show_notes():

    st.title("📝 Notes Generator")

    title = st.text_input(
        "Notes Title",
        "My Study Notes"
    )

    content = st.text_area(
        "Write or Paste Notes",
        height=300
    )

    if st.button("Generate PDF"):

        if content.strip():

            filename = "study_notes.pdf"

            create_pdf(
                title,
                content,
                filename
            )

            with open(filename, "rb") as file:

                st.download_button(
                    "⬇ Download PDF",
                    file,
                    file_name=filename,
                    mime="application/pdf"
                )
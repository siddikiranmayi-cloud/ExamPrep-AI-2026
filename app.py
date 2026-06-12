import streamlit as st
from summary import generate_summary
from quiz import generate_quiz
from qa import answer_question

st.set_page_config(page_title="ExamPrep AI 2026")

st.title("📚 ExamPrep AI 2026")
st.subheader("AI-Powered Study Assistant for Engineering Students")

notes = st.text_area(
    "Paste your study notes here",
    height=200
)

if st.button("Generate Summary"):
    if notes:
        st.success(generate_summary(notes))
    else:
        st.warning("Please enter notes first.")

if st.button("Generate Quiz"):
    quiz = generate_quiz()

    for q in quiz:
        st.write("### " + q["question"])

        for option in q["options"]:
            st.write("- " + option)

        st.write("✅ Answer: " + q["answer"])

question = st.text_input("Ask a question from notes")

if st.button("Answer Question"):
    if notes and question:
        st.info(answer_question(question))
    else:
        st.warning("Enter notes and question.")

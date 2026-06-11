import streamlit as st

st.set_page_config(
    page_title="ExamPrep AI",
    page_icon="📚"
)

st.title("📚 ExamPrep AI")
st.subheader("AI-Powered Study Assistant")

notes = st.text_area(
    "Paste your notes here"
)

if st.button("Generate Summary"):
    st.success("Summary feature coming soon!")

if st.button("Generate Quiz"):
    st.success("Quiz feature coming soon!")

if st.button("Ask Question"):
    st.success("Question Answer feature coming soon!")

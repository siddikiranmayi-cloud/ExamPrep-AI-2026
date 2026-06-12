
import streamlit as st

st.title("ExamPrep AI 2026")

notes = st.text_area("Enter your study notes")

if st.button("Generate Summary"):
    st.write(notes[:100])

if st.button("Generate Quiz"):
    st.write("Q1: What is Artificial Intelligence?")

question = st.text_input("Ask a question")

if st.button("Answer Question"):
    st.write("Answer feature coming soon")


from summary import generate_summary
from quiz import generate_quiz

print("ExamPrep AI 2026")

notes = input("Enter notes: ")

print("\nSummary:")
print(generate_summary(notes))

print("\nQuiz:")
for q in generate_quiz():
    print(q["question"])

# Python Quiz Program - 2 Marks Per Question

quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Python is a programming language. (True/False)",
        "options": [],
        "answer": "True"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "The square root of 16 is:",
        "options": ["A. 2", "B. 4", "C. 8", "D. 16"],
        "answer": "B"
    },
    {
        "question": "HTML stands for HyperText Markup Language. (True/False)",
        "options": [],
        "answer": "True"
    }
]

score = 0
points_per_question = 2
total_marks = len(quiz_data) * points_per_question

print("Welcome to the Quiz!")
print("Each question carries 2 marks.\n")
print("plz choose options only such as ('A','B','C','D')\n")

for i, q in enumerate(quiz_data, start=1):
    print(f"Q{i}: {q['question']}")
    for option in q["options"]:
        print(option)

    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == q["answer"].lower():
        print("Correct!\n")
        score += points_per_question
    else:
        print(f"Wrong! The correct answer is: {q['answer']}\n")

print(f"Your final score is: {score}/{total_marks}")
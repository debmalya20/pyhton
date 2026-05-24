questions = [
    "What is the capital of India?",
    "Who invented Python?",
    "Which planet is called the Red Planet?"
]

options = [
    ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],

    ["A. Elon Musk", "B. Guido van Rossum", "C. Bill Gates", "D. Steve Jobs"],

    ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"]
]

answers = ["A", "B", "C"]

money = 0

for i in range(len(questions)):

    print(f"\nQuestion {i+1}: {questions[i]}")

    for j in options[i]:
        print(f"{j}")

    user_answer = input("Enter your answer (A/B/C/D) = ").upper()

    if user_answer == answers[i]:

        money += 1000

        print(f"Correct Answer!")
        print(f"You won ₹{money}")

    else:

        print(f"Wrong Answer!")
        print(f"You take home ₹{money}")
        break

print(f"\nGame Over")
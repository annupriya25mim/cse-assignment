import random
import time
import os

# -----------------------------
# PYTHON & SOFTWARE QUIZ QUESTIONS
# -----------------------------
QUESTIONS = [
    {
        "question": "Which of the following is an immutable data type in Python?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "C"
    },
    {
        "question": "What does the len() function do?",
        "options": ["A) Returns the length", "B) Returns last element",
                    "C) Deletes element", "D) Sorts a list"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "question": "Which of these is used to handle exceptions?",
        "options": ["A) try–except", "B) throw", "C) catch", "D) error"],
        "answer": "A"
    },
    {
        "question": "What is the output of: print(type({})) ?",
        "options": ["A) list", "B) dict", "C) set", "D) tuple"],
        "answer": "B"
    },
    {
        "question": "Which Python library is used for data manipulation?",
        "options": ["A) NumPy", "B) Pandas", "C) Flask", "D) Tkinter"],
        "answer": "B"
    },
    {
        "question": "Which of these is a valid loop in Python?",
        "options": ["A) for", "B) loop", "C) repeat", "D) iterate"],
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponent in Python?",
        "options": ["A) ^", "B) **", "C) exp()", "D) pow"],
        "answer": "B"
    },
    {
        "question": "What is a correct file extension for Python files?",
        "options": ["A) .py", "B) .pt", "C) .pyn", "D) .python"],
        "answer": "A"
    },
    {
        "question": "What does PIP stand for?",
        "options": ["A) Python Installer Program", "B) Pip Installs Packages",
                    "C) Program Installation Path", "D) Package Import Program"],
        "answer": "B"
    },
    {
        "question": "Which method is used to add an item to a list?",
        "options": ["A) add()", "B) insert()", "C) push()", "D) append()"],
        "answer": "D"
    },
    {
        "question": "Which keyword creates a class?",
        "options": ["A) class", "B) object", "C) defclass", "D) cls"],
        "answer": "A"
    },
    {
        "question": "What is used to import a module?",
        "options": ["A) load", "B) include", "C) import", "D) module"],
        "answer": "C"
    },
    {
        "question": "Which of these is not a Python data type?",
        "options": ["A) int", "B) float", "C) real", "D) str"],
        "answer": "C"
    },
    {
        "question": "In OOP, what does OOP stand for?",
        "options": ["A) Object Oriented Programming", "B) Open Operating Program",
                    "C) Online Object Processing", "D) Open Oriented Program"],
        "answer": "A"
    },
    {
        "question": "Which method is called when an object is created?",
        "options": ["A) __init__", "B) start()", "C) constructor()", "D) new()"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create an anonymous function?",
        "options": ["A) lambda", "B) anon", "C) func", "D) mini"],
        "answer": "A"
    },
    {
        "question": "What is used to convert a string to an integer?",
        "options": ["A) str()", "B) parse()", "C) int()", "D) float()"],
        "answer": "C"
    },
    {
        "question": "Which module is used for regular expressions in Python?",
        "options": ["A) regex", "B) match", "C) re", "D) pyregex"],
        "answer": "C"
    },
    {
        "question": "What is Python primarily known as?",
        "options": ["A) Low-level language", "B) Functional language",
                    "C) High-level programming language", "D) Machine language"],
        "answer": "C"
    }
]

# -----------------------------
# QUIZ APP FUNCTIONS
# -----------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def ask_question(q, question_number, total_questions):
    print(f"\nQuestion {question_number}/{total_questions}")
    print("---------------------------------------------")
    print(q["question"])
    for option in q["options"]:
        print(option)

    answer = input("\nYour answer (A/B/C/D): ").strip().upper()

    if answer == q["answer"]:
        print("✔ Correct!")
        return True
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")
        return False


def start_quiz():
    clear()
    print("=====================================")
    print("      PYTHON QUIZ APPLICATION")
    print("=====================================")

    input("Press Enter to begin...")

    score = 0
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    total_questions = len(questions)

    for idx, q in enumerate(questions, start=1):
        if ask_question(q, idx, total_questions):
            score += 1
        time.sleep(1)
        clear()

    percent = (score / total_questions) * 100

    print("============== RESULTS ==============")
    print(f"Your Score: {score}/{total_questions}")
    print(f"Percentage: {percent:.2f}%")

    if percent >= 90:
        grade = "A+ (Excellent)"
    elif percent >= 75:
        grade = "A"
    elif percent >= 60:
        grade = "B"
    elif percent >= 40:
        grade = "C"
    else:
        grade = "D (Needs improvement)"

    print(f"Grade: {grade}")
    print("=====================================")


def main():
    clear()
    print("=====================================")
    print("      PYTHON QUIZ APPLICATION")
    print("=====================================\n")

    print("1) Start Python Quiz")
    print("2) Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        start_quiz()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

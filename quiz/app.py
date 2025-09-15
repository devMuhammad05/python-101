import random

# list of questions 
# store the answer 

# randomly pick questions 
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score 


questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}


def quiz():
    questions_list = list(questions.keys())
    total_question = 5
    score = 0

    selected_questions = random.sample(questions_list, total_question)

    for index, question in enumerate(selected_questions):
        print(f"{index + 1}. {question}")

        user_answer = input("Your Answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct! \n")
            score += 1
        else:    
            print(f"Wrong. The correct answer is: {correct_answer} \n")

        print(f"Thank you for taking the Quiz your total score is: {score}/{total_question}")

quiz()
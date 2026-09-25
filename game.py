import random
import copy
import string

question_pool = [
    {
        "question": "What is 8 * 7?",
        "options": ["48", "54", "56", "64"],
        "answer": "56"
    },
    {
        "question": "How many sides does a triangle have?",
        "options": ["3", "4", "5", "6"],
        "answer": "3"
    },
    {
        "question": "What is half of 100?",
        "options": ["25", "50", "75", "100"],
        "answer": "50"
    },
    {
        "question": "Which number comes after 999?",
        "options": ["990", "1,000", "1,001", "10,000"],
        "answer": "1,000"
    },
    {
        "question": "What is 25 + 25?",
        "options": ["40", "45", "50", "55"],
        "answer": "50"
    },
    {
        "question": "How many months are there in one year?",
        "options": ["10", "12", "24", "52"],
        "answer": "12"
    },
    {
        "question": "What is the smallest even number?",
        "options": ["0", "1", "2", "4"],
        "answer": "2"
    },
    {
        "question": "How many minutes are in one hour?",
        "options": ["30", "50", "60", "100"],
        "answer": "60"
    },
    {
        "question": "What is 90 ÷ 10?",
        "options": ["8", "9", "10", "90"],
        "answer": "9"
    },
    {
        "question": "Which shape has four equal sides and four right angles?",
        "options": ["A triangle", "A rectangle", "A square", "A circle"],
        "answer": "A square"
    },
    {
        "question": "What is 11 + 9?",
        "options": ["18", "19", "20", "21"],
        "answer": "20"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "What is 5 * 5?",
        "options": ["20", "25", "30", "35"],
        "answer": "25"
    },
    {
        "question": "What is the value of 100 minus 1?",
        "options": ["90", "98", "99", "101"],
        "answer": "99"
    },
    {
        "question": "Which number is greater: 47 or 74?",
        "options": ["47", "74", "They are equal", "None"],
        "answer": "74"
    },
    {
        "question": "What is 18 + 12?",
        "options": ["20", "28", "30", "40"],
        "answer": "30"
    },
    {
        "question": "How many corners does a rectangle have?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is 49 ÷ 7?",
        "options": ["6", "7", "8", "9"],
        "answer": "7"
    },
    {
        "question": "What is 15 + 15 + 15?",
        "options": ["30", "40", "45", "50"],
        "answer": "45"
    },
    {
        "question": "How many digits are in the number 100?",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
    }
]

def display_question(question):
    opt = string.ascii_uppercase[:len(question['options'])]
    print(question['question'])
    for index, option in enumerate(question["options"]):
        print(opt[index], option)
        
def answer_validation(question):
    valid_options = string.ascii_uppercase[:len(question['options'])]
    while True:
        answer = input(f"Select an option {valid_options}: ").strip().upper()
        if answer in valid_options:
            return valid_options.index(answer)
        else:
            print(f"Invalid answer. Please select between {valid_options}.")

def check_answer(question, answer):
    return question['options'][answer] == question['answer']

def display_results(score, total_questions):
    print('-' * 20)
    print("QUIZ COMPLETE")
    print('-' * 20)
    percentage = (score / total_questions) * 100
    print(f"Your final score: {score}/{total_questions}")
    print(f"Percentage: {percentage}%")
    
    if percentage >= 90:
        print("Excellent.")
    elif percentage >= 70:
        print("Very Good.")
    elif percentage >= 50:
        print("Good.")
    else:
        print("Poor. \nKeep Practicing")

def play_again():
    while True:
        play = input("Would you like to play again? (y/n)").strip().lower()
        if play == 'y':
            return True
        elif play == 'n':
            return False
        else:
            print("Enter a valid response (y or n).")

def main():
    while True:
        questions = copy.deepcopy(random.sample(question_pool, 5))
        for question in questions:
            random.shuffle(question['options'])
        score = 0

        for question_num, question in enumerate(questions, start=1):
            print('-' * 20)
            print(f"Question {question_num} of {len(questions)}")
            print('-' * 20)

            display_question(question)

            answer = answer_validation(question)

            if check_answer(question, answer):
                score += 1
                print("\nCORRECT!!!")
                print()
            else:
                print(f"\nWRONG!!!\nCorrect answer is: {question['answer']}.")
                print()

        display_results(score, len(questions))

        if play_again():
            continue
        break

if __name__ == '__main__':
    main()
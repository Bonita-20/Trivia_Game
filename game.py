import random

questions = [
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

# this function takes the user answer and validate
def answer_validation():
    while True:
        answer = input("Select an option (A - D): ").strip().upper()
        if answer == 'A':
            return 0
        elif answer == 'B':
            return 1
        elif answer == 'C':
            return 2
        elif answer == 'D':
            return 3
        else:
            print("Invalid answer. Please select A, B, C, or D.")

def main():
    while True:
        random.shuffle(questions)

        score = 0

        for question_num, question in enumerate(questions, start=1):
            print('-' * 20)
            print(f"Question {question_num} of {len(questions)}")
            print('-' * 20)
            print(question['question'])
            opt = ['A', 'B', 'C', 'D']
            for index, option in enumerate(question["options"]):
                print(opt[index], option)
            answer = answer_validation()
            if question['options'][answer] == question['answer']:
                score += 1
                print("\nCORRECT!!!")
                print()
            else:
                print(f"\nWRONG!!!\nCorrect answer is: {question['answer']}.")
                print()
        print('-' * 20)
        print("QUIZ COMPLETE")
        print('-' * 20)
        percentage = (score / len(questions)) * 100
        print(f"Your final score: {score}/{len(questions)}")
        print(f"Percentage: {percentage}%")

        if percentage >= 90:
            print("Excellent.")
        elif percentage >= 70:
            print("Very Good.")
        elif percentage >= 50:
            print("Good.")
        else:
            print("Poor. \nKeep Practicing")
        while True:
            play_again = input("Would you like to play again? (y/n)").strip().lower()
            if play_again == 'y':
                break
            elif play_again == 'n':
                return
            else:
                print("Enter a valid response (y or n).")

if __name__ == '__main__':
    main()
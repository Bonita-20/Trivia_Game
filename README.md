# Python Quiz Game 🧠

A simple command-line mathematics quiz game built with Python. The project was created as a beginner-friendly way to practice core Python programming concepts including functions, lists, dictionaries, loops, conditionals, input validation, randomization, and program flow.

## 📌 Overview

The Python Quiz Game presents the user with a randomized set of mathematics questions. Each question contains multiple-choice answers, and the user selects an answer using the corresponding letter.

The game:

* Randomly selects 5 questions from a pool of 20.
* Randomizes the order of the answer options.
* Accepts answers using option letters such as A, B, C, or D.
* Validates user input.
* Checks whether the selected answer is correct.
* Keeps track of the user's score.
* Displays the final score and percentage.
* Provides performance feedback.
* Clears the terminal between questions for a cleaner quiz experience.
* Allows the user to play another round.

## ✨ Features

### 🎲 Randomized Questions

Each game selects 5 unique questions from the question pool using Python's `random.sample()`.

### 🔀 Randomized Answer Options

The answer choices are shuffled for every selected question using `random.shuffle()`.

### 🛡️ Protected Question Data

`copy.deepcopy()` is used to create an independent copy of the selected questions before their options are shuffled. This prevents changes to the original question pool.

### 🔤 Dynamic Answer Options

Option labels are generated dynamically using `string.ascii_uppercase`.

This means the program can support different numbers of options without hard-coding labels such as A, B, C, and D.

### ✅ Input Validation

The program validates the user's answer and continues asking until a valid option is entered.

It accepts both uppercase and lowercase input and removes unnecessary spaces from the user's response.

### 🧮 Automatic Scoring

The program keeps track of correct answers and calculates the user's final percentage.

### 📊 Performance Feedback

At the end of the quiz, the program provides feedback based on the user's percentage.

### 🖥️ Terminal Screen Clearing

The terminal is cleared after each question so that previous questions and answers do not remain visible.

The project uses the appropriate terminal command based on the operating system:

* Windows → `cls`
* Linux/macOS → `clear`

This creates a cleaner, more focused quiz interface.

### 🔁 Replay

After completing a quiz, the user can choose whether to start another round.

## 🛠️ Technologies Used

* Python 3
* `random`
* `copy`
* `string`
* `os`

## 📂 Project Structure

```text
quiz-game/
│
├── quiz_game.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Bonita-20/Trivia_Game.git
```

### 2. Navigate into the project directory

```bash
cd Trivia_Game
```

### 3. Run the program

```bash
python3 game.py
```

On systems where Python is configured as `python`, you can also use:

```bash
python game.py
```

## 🎮 How to Play

1. Start the program.
2. The game randomly selects 5 questions.
3. Read the question and available options.
4. Enter the corresponding option letter.
5. The program tells you whether your answer is correct.
6. Press **Enter** to continue.
7. The terminal is cleared before the next question is displayed.
8. After all 5 questions, your final score and percentage are displayed.
9. Choose whether to play again.

### Example

```text
====================
MATHEMATICS QUIZ
====================

Question 1 of 5
--------------------
What is 8 * 7?
A. 48
B. 54
C. 56
D. 64

Select an option A-D: C

CORRECT!!!

Press Enter to continue...
```

After pressing Enter, the previous question is cleared and the next question is displayed on a clean terminal screen.

## 📚 Python Concepts Practiced

This project was built to practice the following Python concepts:

* Variables
* Lists
* Dictionaries
* Nested data structures
* Functions
* Function parameters and arguments
* Return values
* `for` loops
* `while` loops
* `enumerate()`
* Conditional statements
* Boolean expressions
* String manipulation
* String slicing
* String indexing
* Membership testing with `in`
* List indexing
* Randomization
* `random.sample()`
* `random.shuffle()`
* Deep copying with `copy.deepcopy()`
* Input validation
* Exception-resistant input handling
* Operating-system interaction with `os`
* Cross-platform terminal commands
* Program flow
* Basic command-line interface (CLI) design
* Separation of data from program logic

## 📊 Scoring

The quiz contains 5 questions per round.

The final percentage is calculated as:

```text
(score / total questions) × 100
```

Performance feedback is then displayed based on the percentage achieved.

## 🔮 Future Improvements

Possible future improvements include:

* Add different quiz categories.
* Allow the user to choose the number of questions.
* Add difficulty levels.
* Add a timer for each question.
* Store high scores.
* Save quiz results to a file.
* Add more question pools.
* Add explanations for correct answers.
* Add a leaderboard.
* Add colored terminal output.
* Load questions from an external JSON file.
* Add automated tests.

## 🎯 Learning Purpose

This project is part of my journey to strengthen my Python programming fundamentals through practical projects.

Rather than focusing only on syntax, the project applies Python concepts to a complete, interactive command-line application.

## 👩🏾‍💻 Author

**Nwamaka Precious Chidiebere**

Statistics Graduate | Data Scientist | Python Learner

* LinkedIn: https://linkedin.com/in/chidiebere-nwamaka-precious
* GitHub: https://github.com/Bonita-20

## 📄 License

This project is available for educational and personal use.

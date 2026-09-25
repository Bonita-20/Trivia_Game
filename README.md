# 🎯 Python Quiz Game

A terminal-based multiple-choice quiz game built with Python. The project demonstrates core Python programming concepts including functions, lists, dictionaries, loops, conditionals, input validation, randomization, and working with mutable objects and deep copies.

## 📌 Project Overview

This Quiz Game presents the player with **5 randomly selected questions** from a predefined question pool. Each question contains multiple-choice answers, and the options are randomized for every game.

The player selects an answer, receives immediate feedback, and earns one point for each correct response. At the end of the game, the program calculates the player's percentage score and provides a performance message.

The game also allows the player to start a new round without restarting the program.

## ✨ Features

* 🎲 Randomly selects 5 questions from the question pool
* 🔀 Randomizes the order of answer options
* 📝 Displays multiple-choice questions
* ✅ Validates user input
* 🎯 Checks answers automatically
* 📊 Calculates and displays the final score
* 📈 Calculates the player's percentage
* 🔁 Supports replaying the quiz
* 🔤 Dynamically generates option labels (`A`, `B`, `C`, `D`, etc.)
* 🛡️ Uses deep copies to prevent modification of the original question data
* 💻 Runs directly in the terminal

## 🛠️ Technologies Used

* **Python 3**
* `random` — question and option randomization
* `copy` — deep copying of nested data structures
* `string` — dynamic generation of option labels

No external packages are required.

## 📂 Project Structure

```text
Quiz_Game/
│
├── game.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Trivia_Game.git
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

1. The game randomly selects 5 questions.
2. Each question is displayed with its available options.
3. Enter the corresponding option letter.
4. The program validates your input.
5. You receive immediate feedback indicating whether your answer was correct.
6. After all questions have been answered, your final score and percentage are displayed.
7. Choose whether to play another round.

Example:

```text
--------------------
Question 1 of 5
--------------------
What is 8 * 7?
A 48
B 54
C 56
D 64

Select an option ABCD: C

CORRECT!!!
```

## 🧠 Python Concepts Practiced

This project was developed as a hands-on exercise to strengthen foundational Python programming skills.

### Data Structures

* Lists
* Dictionaries
* Nested data structures
* List indexing
* String slicing

### Control Flow

* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* `break`
* `continue`

### Functions

The program separates different responsibilities into reusable functions:

* `display_question()`
* `answer_validation()`
* `check_answer()`
* `display_results()`
* `play_again()`
* `main()`

### Randomization

The project uses:

```python
random.sample()
```

to select unique questions and:

```python
random.shuffle()
```

to randomize the answer options.

### Input Validation

User input is normalized using:

```python
.strip().upper()
```

This allows inputs such as `a`, `A`, or `A` to be handled consistently.

### Mutable Objects and Deep Copying

The project uses:

```python
copy.deepcopy()
```

to create independent copies of selected questions before their answer options are shuffled.

This prevents the original `question_pool` from being modified during gameplay.

### Dynamic Option Handling

Rather than hard-coding `A`, `B`, `C`, and `D`, the program generates option labels based on the number of available choices:

```python
string.ascii_uppercase[:len(question["options"])]
```

This allows the quiz structure to support additional answer choices without changing the validation logic.

## 📊 Scoring

The game awards **1 point for each correct answer**.

The final percentage is calculated using:

```text
Percentage = (Score / Total Questions) × 100
```

Performance feedback is then displayed based on the resulting percentage.

## 🔮 Possible Future Improvements

Future versions of the project could include:

* [ ] Difficulty levels
* [ ] Multiple quiz categories
* [ ] Larger question banks
* [ ] Timer-based questions
* [ ] Persistent high scores
* [ ] Player names and profiles
* [ ] Loading questions from a JSON file
* [ ] Saving quiz results
* [ ] A graphical user interface
* [ ] Unit tests
* [ ] More advanced question types

## 🎓 Learning Purpose

This project was created as part of my hands-on Python learning journey. The focus was not only on making the program work, but also on understanding how Python handles:

* Data structures
* Functions and program flow
* Input validation
* Randomization
* Mutable objects
* Copying nested data
* Modular program design

The project represents a progression from basic Python syntax toward writing more structured and maintainable programs.

## 👤 Author

**Nwamaka Precious Chidiebere**

Statistician | Data Scientist | Python Learner

* LinkedIn: [linkedin.com/in/chidiebere-nwamaka-precious](https://linkedin.com/in/chidiebere-nwamaka-precious)
* GitHub: [github.com/Yafah-B](https://github.com/Bonita-20)

## 📄 License

This project is available for educational and personal learning purposes.

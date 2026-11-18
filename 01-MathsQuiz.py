from tkinter import *
from tkinter import messagebox
import random

# === START SETUP ===

root = Tk()
root.title("Ye Olde Maths Quiz")
root.geometry("500x700")
root.resizable(0, 0)

BG = "#FFF5E3"
score = 0
root.config(bg=BG)

# === QUIZ DICTIONARY ===

# A dictionary that contains the base of the quiz's information
quiz = {
    "difficulty" : 1,
    "operation" : "+",
    "answer" : 0,
    "question" : 1,
    "attempt" : 1
}

# === FUNCTIONS ===

# Displays the difficulty level menu when you first open the quiz
def displayMenu():
    menu_frame.tkraise()

# Defines the values based on the difficulty selected
def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1000, 9999)

# The function that randomizes the operation in the questions
def decideOperation():
    if random.randint(1, 2) == 1:
        return '+'
    else:
        return '-'

# Displays the problem and takes in the user's answer
def displayProblem(difficulty):
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()

    if operation == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2

    quiz["difficulty"] = difficulty
    quiz["operation"] = operation
    quiz["answer"] = answer
    quiz["attempt"] = 1

    problem_label.config(text=f"{num1} {operation} {num2} = ?")
    score_label.config(text=f"Score: {score}")
    question_label.config(text=f"Question {quiz["question"]} out of 10")
    feedback_label.config(text="")
    answer_entry.delete(0, END)

# The function that checks the user's answer and gives feedback accordingly
def isCorrect():
    global score
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_label.config(text="Please enter a number!")
        return

    answer_entry.delete(0, END)
    
    if user_answer == quiz["answer"]:
        if quiz["attempt"] == 1:
            score += 10
        else:
            score += 5
        feedback_label.config(text="Correct!")
        score_label.config(text=f"Score: {score}")
        quiz["question"] += 1
        submit_button.config(text="Next", command=nextQuestion)

    elif quiz["attempt"] == 1:
        quiz["attempt"] = 2
        feedback_label.config(text="Wrong! Try again for half points.")

    else:
        feedback_label.config(text=f"Wrong! The answer was {quiz["answer"]}.")
        quiz["question"] += 1
        submit_button.config(text="Next", command=nextQuestion)

# This function moves to the next question in the quiz
def nextQuestion():
    submit_button.config(text="Submit", command=isCorrect)
    if quiz["question"] == 11:
        displayResults()
    else:
        displayProblem(quiz["difficulty"])

# Outputs the user's final score out of 100 and gives a rank (e.g. A+ for a score over 90)
def displayResults():
    global score
    if score > 90:
        rank_score = "A+"
    elif score >= 80:
        rank_score = "A"
    elif score >= 70:
        rank_score = "B"
    elif score >= 50:
        rank_score = "C"
    else:
        rank_score = "F"
    
    result_label.config(text=f"Your Score: {score} out of 100")
    rank_label.config(text=f"Your Overall Rank: {rank_score}")
    results_frame.tkraise()

# The function that starts and sets the quiz
def startQuiz(difficulty, frame):
    global score
    score = 0
    quiz["question"] = 1
    displayProblem(difficulty)
    switch_to_frame(frame)

def replayQuiz():
    answer = messagebox.askyesno("Play Again", "Shall we play again?")
    if answer:
        displayMenu()
    else:
        rank_label.config(text="Until next time!")

def switch_to_frame(frame):
    frame.tkraise()

# === MENU FRAME ===

menu_frame = Frame(root, bg=BG)
menu_label = Label(menu_frame, text="Welcome brave traveler to the Ye Olde Maths Quiz Tavern!", font=("Bookman Old Style", 12), bg=BG, fg="#594529")
menu_label.pack(pady=5)
menu_label = Label(menu_frame, text="Please select thy difficulty:", font=("Lucida Console", 10), bg=BG, fg="#594529")
menu_label.pack(pady=5)

# Easy Button
easy_button = Button(menu_frame, text="Easy", font=("Lucida Console", 10), bg=BG, fg="#594529", command=lambda: [startQuiz(1, easy_frame)])
easy_button.pack(pady=10)

# Moderate Button
moderate_button = Button(menu_frame, text="Moderate", font=("Lucida Console", 10), bg=BG, fg="#594529", command=lambda: [startQuiz(2, moderate_frame)])
moderate_button.pack(pady=10)

# Advanced Button
advanced_button = Button(menu_frame, text="Advanced", font=("Lucida Console", 10), bg=BG, fg="#594529", command=lambda: [startQuiz(3, advanced_frame)])
advanced_button.pack(pady=10)

menu_frame.place(x=0, y=0, width=500, height=700)

# === EASY DIFFICULTY FRAME ===

easy_frame = Frame(root, bg=BG)

easy_label = Label(easy_frame, text="This is the Easy Quiz!", font=("Lucida Console", 12), bg=BG, fg="#594529")
easy_label.pack(pady=10)
question_label = Label(easy_frame, text=f"Question {quiz["question"]} of 10", font=("Lucida Console", 12), bg=BG, fg="#594529")
question_label.pack(pady=10)
score_label = Label(easy_frame, text=f"Score: {score}", font=("Lucida Console", 12), bg=BG, fg="#594529")
score_label.pack(pady=10)
problem_label = Label(easy_frame, text="", font=("Lucida Console", 12), bg=BG, fg="#594529")
problem_label.pack(pady=10)
answer_entry = Entry(easy_frame, font=("Lucida Console", 12), bg=BG, fg="#594529")
answer_entry.pack(pady=10)
submit_button = Button(easy_frame, text="Submit", font=("Lucida Console", 12), bg=BG, fg="#594529", command=isCorrect)
submit_button.pack(pady=10)
feedback_label = Label(easy_frame, text="", font=("Lucida Console", 12), bg=BG, fg="#594529")
feedback_label.pack(pady=10)

easy_frame.place(x=0, y=0, width=500, height=700)

# === RESULTS FRAME ===

results_frame = Frame(root, bg=BG)
title_label = Label(results_frame, text="Ye did it! Congrats dear wanderer!", font=("Lucida Console", 12), bg=BG, fg="#594529")
title_label.pack(pady=10)
result_label = Label(results_frame, text="", font=("Lucida Console", 12), bg=BG, fg="#594529")
result_label.pack(pady=10)
rank_label = Label(results_frame, text="", font=("Lucida Console", 12), bg=BG, fg="#594529")
rank_label.pack(pady=10)
replay_button = Button(results_frame, text="Would thou like to play again?", font=("Lucida Console", 12), bg=BG, fg="#594529", command=replayQuiz)
replay_button.pack(pady=10)

results_frame.place(x=0, y=0, width=500, height=700)

# === END SETUP ===

displayMenu()
root.mainloop()
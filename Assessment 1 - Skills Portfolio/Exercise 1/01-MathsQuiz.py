from tkinter import *
from tkinter import messagebox
import random
import pygame
from PIL import ImageTk, Image

# === START SETUP ===

root = Tk()
root.title("⋆⊱༻ཐི Witch's Apprentice ཋྀ༺⊰⋆")
root.geometry("500x700")
root.resizable(0, 0)
root.iconbitmap("Assessment 1 - Skills Portfolio\Exercise 1\Assets\icon.ico")

BG = "#fffde5"
score = 0
root.config(bg=BG)

# == MUSIC ==

pygame.mixer.init()
pygame.mixer.music.load(r"Assessment 1 - Skills Portfolio\Exercise 1\Assets\bg_music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)
music_on = True

def toggleMusic():
    global music_on
    if music_on:
        pygame.mixer.music.pause()
        music_button.config(text="🔇 Music: Off")
    else:
        pygame.mixer.music.unpause()
        music_button.config(text="🔊 Music: On")
    music_on = not music_on

music_button = Button(root, text="🔊 Music: On", font=("Candara", 10), bg="#1c1f43", fg="#f8f4c2", command=toggleMusic)
music_button.place(x=395, y=25)

bell_sound = pygame.mixer.Sound(r"Assessment 1 - Skills Portfolio\Exercise 1\Assets\bell.wav")
bell_sound.set_volume(0.8)

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

def displayTitle():
    title_frame.tkraise()
    music_button.lift()

# Displays the difficulty level menu when you first open the quiz
def displayMenu():
    menu_frame.tkraise()

def beginQuiz():
    bell_sound.play()
    displayMenu()

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
    answer_entry.delete(0, END)

# The function that checks the user's answer and gives feedback accordingly
def isCorrect():
    global score
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showwarning("Hold on!", "Please enter a number!")
        return

    answer_entry.delete(0, END)
    
    if user_answer == quiz["answer"]:
        if quiz["attempt"] == 1:
            score += 10
        else:
            score += 5
        score_label.config(text=f"Score: {score}")
        quiz["question"] += 1
        messagebox.showinfo("Correct!", "Correct!")
        nextQuestion()

    elif quiz["attempt"] == 1:
        quiz["attempt"] = 2
        messagebox.showwarning("Wrong!", "Wrong! Try again for half points.")

    else:
        quiz["question"] += 1
        messagebox.showerror("Wrong!", f"Wrong! THe answer was {quiz["answer"]}")
        nextQuestion()

# This function moves to the next question in the quiz
def nextQuestion():
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
def startQuiz(difficulty):
    global score
    score = 0
    quiz["question"] = 1
    displayProblem(difficulty)
    quiz_frame.tkraise()

def replayQuiz():
    answer = messagebox.askyesno("Play Again", "Shall we play again?")
    if answer:
        displayMenu()
    else:
        rank_label.config(text="Until next time!")

# Back to Start Button
def backToMenu():
    if messagebox.askyesno("Go Back", "Return to the menu? Thy current progress will be lost"):
        displayMenu()

# === TITLE FRAME ===

title_frame = Frame(root, bg=BG)

try:
    bg_image = ImageTk.PhotoImage(Image.open(r"Assessment 1 - Skills Portfolio\Exercise 1\Assets\title_background.png").resize((500, 700)))
    bg_label = Label(title_frame, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except (FileNotFoundError, OSError):
    pass

start_button = Button(title_frame, text="Begin", font=("Bookman Old Style", 12), bg="#1c1f43", fg="#f8f4c2", command=beginQuiz)
start_button.place(relx=0.5, rely=0.85, anchor=CENTER)

title_frame.place(x=0, y=0, width=500, height=700)

# === MENU FRAME ===

menu_frame = Frame(root, bg=BG)

menu_bg_image = ImageTk.PhotoImage(Image.open(r"Assessment 1 - Skills Portfolio\Exercise 1\Assets\menu_background.png").resize((500, 700)))
menu_bg_label = Label(menu_frame, image=menu_bg_image).place(x=0, y=0, relwidth=1, relheight=1)

menu_label = Label(menu_frame, text="You enter the guild house...", font=("Bookman Old Style", 12), bg="#c1a37f", fg="#251c18").pack(pady=45)
text_label = Label(menu_frame, text="\"Ah, the new hire has finally arrived!\"", font=("Candara", 12), bg="#fffde5", fg="#251c18").pack(padx=(30, 0), pady=20, anchor="w")
text_label = Label(menu_frame, text="\"I am Head Witch Circe and welcome\nto your first day as an apprentice.\nYou have classes today with our\nfinest brewers.\"", font=("Candara", 12), bg="#fffde5", fg="#251c18", justify=LEFT).pack(padx=(30, 0), anchor="w")
menu_label = Label(menu_frame, text="\"Head to one of your lessons when\nyou're ready.\"", font=("Candara", 12), bg=BG, fg="#251c18", justify=LEFT).pack(padx=(30, 0), pady=15, anchor="w")

# Easy Button
easy_button = Button(menu_frame, text="˚.⋆꒰১ Easy Lesson in Mana Elixirs ໒꒱⋆.˚", font=("Candara", 12), bg="#92633e", fg="#fffde5", command=lambda: [startQuiz(1)])
easy_button.pack(pady=(130, 8))

# Moderate Button
moderate_button = Button(menu_frame, text="⋆˖⁺‧₊☽ Moderate Lesson in Nightshade Poisons ☾₊‧⁺˖⋆", font=("Candara", 12), bg="#92633e", fg="#fffde5", command=lambda: [startQuiz(2)])
moderate_button.pack(pady=8)

# Advanced Button
advanced_button = Button(menu_frame, text="⁺‧₊˚ ཐི⋆ Advanced Lesson in Love Potions ⋆ཋྀ ˚₊‧⁺", font=("Candara", 12), bg="#92633e", fg="#fffde5", command=lambda: [startQuiz(3)])
advanced_button.pack(pady=8)

menu_frame.place(x=0, y=0, width=500, height=700)

# === QUIZ FRAME ===

quiz_frame = Frame(root, bg=BG)

question_label = Label(quiz_frame, text=f"Question {quiz["question"]} of 10", font=("Candara", 12), bg=BG, fg="#251c18")
question_label.pack(pady=10)
score_label = Label(quiz_frame, text=f"Score: {score}", font=("Candara", 12), bg=BG, fg="#251c18")
score_label.pack(pady=10)
problem_label = Label(quiz_frame, text="", font=("Candara", 12), bg=BG, fg="#251c18")
problem_label.pack(pady=10)
answer_entry = Entry(quiz_frame, font=("Candara", 12), bg=BG, fg="#251c18")
answer_entry.pack(pady=10)
submit_button = Button(quiz_frame, text="Submit", font=("Candara", 12), bg=BG, fg="#251c18", command=isCorrect)
submit_button.pack(pady=10)
back_button = Button(quiz_frame, text="Back to Menu", font=("Candara", 12), bg=BG, fg="#251c18", command=backToMenu)
back_button.pack(pady=10)

quiz_frame.place(x=0, y=0, width=500, height=700)

# === RESULTS FRAME ===

results_frame = Frame(root, bg=BG)
title_label = Label(results_frame, text="Ye did it! Congrats dear wanderer!", font=("Candara", 12), bg=BG, fg="#251c18")
title_label.pack(pady=10)
result_label = Label(results_frame, text="", font=("Candara", 12), bg=BG, fg="#251c18")
result_label.pack(pady=10)
rank_label = Label(results_frame, text="", font=("Candara", 12), bg=BG, fg="#251c18")
rank_label.pack(pady=10)
replay_button = Button(results_frame, text="Would thou like to play again?", font=("Candara", 12), bg=BG, fg="#251c18", command=replayQuiz)
replay_button.pack(pady=10)

results_frame.place(x=0, y=0, width=500, height=700)

# === END SETUP ===

displayTitle()
root.mainloop()
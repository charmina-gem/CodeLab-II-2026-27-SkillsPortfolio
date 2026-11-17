from tkinter import *   
import random 

# === START SETUP ===

root = Tk()
root.title("Ye Olde Maths Quiz")
root.geometry("500x700")
root.resizable(0, 0)

BG = "#FFF5E3"
score = 0
root.config(bg=BG)

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
        return random.randint(100, 999)

def decideOperation():
    if random.randint(1, 2) == 1:
        return '+'
    else:
        return '-'

# def displayProblem():

# def isCorrect():

def displayResults():
    score = 0

def switch_to_frame(frame):
    frame.tkraise()

# === MENU FRAME ===

menu_frame = Frame(root, bg=BG)
menu_label = Label(menu_frame, text="Welcome brave traveler to the Ye Olde Maths Quiz Tavern!", font=("Bookman Old Style", 12), bg=BG, fg="#594529")
menu_label.pack(pady=5)
menu_label = Label(menu_frame, text="Please select thy difficulty:", font=("Lucida Console", 10), bg=BG, fg="#594529")
menu_label.pack(pady=5)

# Easy Button
easy_button = Button(menu_frame, text="Easy", font=("Lucida Console", 10), bg=BG, fg="#594529", command=lambda: switch_to_frame(easy_frame))
easy_button.pack(pady=10)

# Moderate Button
moderate_button = Button(menu_frame, text="Moderate", font=("Lucida Console", 10), bg=BG, fg="#594529", command=lambda: switch_to_frame(moderate_frame))
moderate_button.pack(pady=10)

# Advanced Button
advanced_button = Button(menu_frame, text="Advanced", font=("Lucida Console", 10), bg=BG, fg="#594529", command=lambda: switch_to_frame(advanced_frame))
advanced_button.pack(pady=10)

menu_frame.place(x=0, y=0, width=500, height=700)

# === EASY DIFFICULTY FRAME ===

easy_frame = Frame(root, bg=BG)

easy_label = Label(easy_frame, text="This is the Easy Quiz!", font=("Lucida Console", 12), bg=BG, fg="#594529")
easy_label.pack(pady=10)
easy_question = Label(easy_frame, text="Question 1 of 10", font=("Lucida Console", 12), bg=BG, fg="#594529")
easy_question.pack(pady=10)
score_label = Label(easy_frame, text=f"Score: {score}", font=("Lucida Console", 12), bg=BG, fg="#594529")
score_label.pack(pady=10)

easy_frame.place(x=0, y=0, width=500, height=700)

# === MODERATE DIFFICULTY FRAME ===

moderate_frame = Frame(root, bg=BG)

moderate_label = Label(moderate_frame, text="This is the Moderate Quiz!", font=("Lucida Console", 12), bg=BG, fg="#594529")
moderate_label.pack(pady=10)

moderate_frame.place(x=0, y=0, width=500, height=700)

# === ADVANCED DIFFICULTY FRAME ===

advanced_frame = Frame(root, bg=BG)

advanced_label = Label(advanced_frame, text="This is the Advanced Quiz!", font=("Lucida Console", 12), bg=BG, fg="#594529")
advanced_label.pack(pady=10)

advanced_frame.place(x=0, y=0, width=500, height=700)

# === END SETUP ===

displayMenu()
root.mainloop()
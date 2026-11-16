from tkinter import *    

# === START SETUP ===

root = Tk()
root.title("Ye Olde Maths Quiz")
root.geometry("500x700")
root.resizable(0, 0)

BG = "#EDE0D5"
root.config(bg=BG)

# === FUNCTIONS ===

# Displays the difficulty level menu when you first open the quiz
def displayMenu():
    menu_frame.tkraise()

# def randomInt():

# def decideOperation():

# def displayProblem():

# def isCorrect():

# def displayResults():

def switch_to_frame(frame):
    frame.tkraise()

# === MENU FRAME ===

menu_frame = Frame(root)
menu_label = Label(menu_frame, text="Welcome brave traveler to the Ye Olde Maths Quiz Tavern!", font=("Bookman Old Style", 12), fg="black")
menu_label.pack(pady=5)
menu_label = Label(menu_frame, text="Please select thy difficulty", font=("Lucida Console", 10), fg="black")
menu_label.pack(pady=5)

# Easy Button
easy_button = Button(menu_frame, text="Easy", font=("Lucida Console", 10), fg="black", command=lambda: switch_to_frame(easy_frame))
easy_button.pack(pady=10)

# Moderate Button
moderate_button = Button(menu_frame, text="Moderate", font=("Lucida Console", 10), fg="black", command=lambda: switch_to_frame(moderate_frame))
moderate_button.pack(pady=10)

# Advanced Button
advanced_button = Button(menu_frame, text="Advanced", font=("Lucida Console", 10), fg="black", command=lambda: switch_to_frame(advanced_frame))
advanced_button.pack(pady=10)

menu_frame.place(x=0, y=0, width=500, height=700)

# === EASY DIFFICULTY FRAME ===

easy_frame = Frame()

easy_label = Label(easy_frame, text="This is the Easy Quiz!", font=("Lucida Console", 12), fg="black")
easy_label.pack(pady=10)

easy_frame.place(x=0, y=0, width=500, height=700)

# === MODERATE DIFFICULTY FRAME ===

moderate_frame = Frame()

moderate_label = Label(moderate_frame, text="This is the Moderate Quiz!", font=("Lucida Console", 12), fg="black")
moderate_label.pack(pady=10)

moderate_frame.place(x=0, y=0, width=500, height=700)

# === ADVANCED DIFFICULTY FRAME ===

advanced_frame = Frame()

advanced_label = Label(advanced_frame, text="This is the Advanced Quiz!", font=("Lucida Console", 12), fg="black")
advanced_label.pack(pady=10)

advanced_frame.place(x=0, y=0, width=500, height=700)

# === END SETUP ===

menu_frame.tkraise()
root.mainloop()
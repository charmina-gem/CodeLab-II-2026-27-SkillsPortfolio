from tkinter import *
import random

# === START SETUP ===

root = Tk()
root.title("Joke Generator")
root.geometry("400x400")
root.resizable(0, 0)

BG = "#FFF5E3"
root.config(bg=BG)

# === FUNCTIONS ===

# Displays the starting screen to the joke generator
def displayStart():
    start_frame.tkraise()

# When the button is clicked, randomly select a joke from the randomJokes.txt file, display the setup of the joke in a label
def generateJoke():
    joke_frame.tkraise()

# Include a "Next Joke" button so the user can request another random joke.
# def nextJoke():
    # ads

# Provide another button labeled "Show Punchline"- When clicked, display the punchline below the setup.
# def showPunchline():
    # asd

# === START FRAME ===

start_frame = Frame(root, bg=BG)

start_label = Label(start_frame, text="Welcome to your personal joke assistant!", font="Georgia", bg=BG, fg="black")
start_label.pack(pady=10)
start_button = Button(start_frame, text="Want to hear a joke?", font="Georgia", bg=BG, fg="black", command=generateJoke)
start_button.pack(pady=10)

start_frame.place(x=0, y=0, width=400, height=400)

# === JOKE FRAME ===

joke_frame = Frame(root, bg=BG)

next_button = Button(joke_frame, text="Next Joke", font="Georgia", bg=BG, fg="black", command=nextJoke)
next_button.pack(pady=10)
punchline_button = Button(joke_frame, text="Show Punchline", font="Georgia", bg=BG, fg="black", command=nextJoke)
punchline_button.pack(pady=10)

# Additionally , provide a "Quit" button to close the application.
end_button = Button(joke_frame, text="Quit", font="Georgia", bg=BG, fg="black", command=root.destroy)
end_button.pack(pady=10)

joke_frame.place(x=0, y=0, width=400, height=400)

# === END SETUP ===

displayStart()
root.mainloop()
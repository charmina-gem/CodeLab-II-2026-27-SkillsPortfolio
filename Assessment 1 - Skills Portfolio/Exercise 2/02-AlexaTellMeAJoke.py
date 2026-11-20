from tkinter import *
import random

# === START SETUP ===

root = Tk()
root.title("Joke Generator")
root.geometry("400x400")
root.resizable(0, 0)

BG = "#FFF5E3"
root.config(bg=BG)

# === JOKE DICTIONARY ===
current = {
    "punchline": ""
}

# === FUNCTIONS ===

# Displays the starting screen to the joke generator
def displayStart():
    start_frame.tkraise()

def generateJokes():
    jokes = []
    with open("Assessment 1 - Skills Portfolio/Exercise 2/randomJokes.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().replace("- ", "", 1)
        if "?" in line:
            jokes_separate = line.split("?", 1)
            jokes.append([jokes_separate[0] + "?", jokes_separate[1]])
    return jokes

# When the button is clicked, randomly select a joke from the randomJokes.txt file, display the setup of the joke in a label
def displayJoke():
    num = random.randint(0, len(jokes) - 1)
    joke_label.config(text=jokes[num][0])
    punchline_label.config(text="")
    current["punchline"] = jokes[num][1]
    joke_frame.tkraise()

# Include a "Next Joke" button so the user can request another random joke.
# def nextJoke():
    # ads

# Provide another button labeled "Show Punchline"- When clicked, display the punchline below the setup.
# def showPunchline():
    # asd

jokes = generateJokes()

# === START FRAME ===

start_frame = Frame(root, bg=BG)

start_label = Label(start_frame, text="Welcome to your personal joke assistant!", font=("Georgia, 10"), bg=BG, fg="black")
start_label.pack(pady=10)
start_button = Button(start_frame, text="Want to hear a joke?", font=("Georgia, 10"), bg=BG, fg="black", command=displayJoke)
start_button.pack(pady=10)

start_frame.place(x=0, y=0, width=400, height=400)

# === JOKE FRAME ===

joke_frame = Frame(root, bg=BG)

joke_label = Label(joke_frame, text="", font=("Georgia, 10"), bg=BG, fg="black")
joke_label.pack(pady=10)
punchline_label = Label(joke_frame, text="", font=("Georgia, 10"), bg=BG, fg="black")
punchline_label.pack(pady=10)
next_button = Button(joke_frame, text="Next Joke", font=("Georgia, 10"), bg=BG, fg="black") #command=nextJoke)
next_button.pack(pady=10)
punchline_button = Button(joke_frame, text="Show Punchline", font=("Georgia, 10"), bg=BG, fg="black") #command=showPunchline)
punchline_button.pack(pady=10)

# Additionally , provide a "Quit" button to close the application.
end_button = Button(joke_frame, text="Quit", font=("Georgia, 10"), bg=BG, fg="black", command=root.destroy)
end_button.pack(pady=10)

joke_frame.place(x=0, y=0, width=400, height=400)

# === END SETUP ===

displayStart()
root.mainloop()
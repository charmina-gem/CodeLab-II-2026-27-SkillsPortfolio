from tkinter import ttk, messagebox
import tkinter as tk

# === START SETUP ===

root = Tk()
root.title("Student Manager")
root.geometry("600x700")
root.resizable(0,0)

BG = "#FFF5E3"
root.config(bg=BG)

# === VARIABLES ===

student_name: tk.StringVar()
student_num: tk.StringVar()
course1: tk.StringVar()
course2: tk.StringVar()
course3: tk.StringVar()
exam: tk.StringVar()

# === FUNCTIONS ===

# data is separated into number of students, student code (between 1000 and 9999), three course marks (out of 20), and examination mark (out of 100)

# should be able to view all student records 
# students name, students number, total coursework mark, exam mark, overall percentage (based on the potential of 160 marks), student grade (A for 70%+, B for 60-69%, C for 50-59%, D for 40-49%, F for under 40%)
# there should be a summary stating the number of students in the class and average percentage mark obtained
# add a sort by ascending and descending order filter

# view individual student record
# allows the user to select a student thenoutput their resutls as per menu item
# how you enable the user to select the student is up to you (either a menu code or by searching the student's name/number)

# show student with the highest and lowest total score
# identify the student with the highest mark and output their results in same format

def displayMenu():
    menu_frame.tkraise()

# def displayRecords():

# make it so that you can add new data/new students with all the required information
# you should also be able to delete records by selecting a student by name or student number to delete their info from the file
# allow the user to be able to select a student by name or student number to update their records - use a sub-menu to edit specific items
# def newRecord():


# === MAIN MENU FRAME ===

menu_frame = Frame(root, bg=BG)

menu_label = Label(menu_frame, text="Student Management System", font=("Georgia", 12), bg=BG, fg="black")
menu_label.pack(pady=10)

# == FORM FRAME ==

form_label = Label(menu_frame, text="Student Details", font=("Georgia", 12), bg=BG, fg="black")
form_label.pack(pady=10)

menu_frame.place(x=0, y=0, width=600, height=700)

# === END SETUP ===

displayMenu()
root.mainloop()
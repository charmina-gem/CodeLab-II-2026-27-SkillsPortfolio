from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# === START SETUP ===

root = Tk()
root.title("Student Manager")
root.geometry("900x500")
root.resizable(0,0)

BG = "#FFF5E3"
root.config(bg=BG)

# === VARIABLES ===

student_name: StringVar()
student_num: StringVar()
course1: StringVar()
course2: StringVar()
course3: StringVar()
exam: StringVar()

DATA_FILE = "studentMarks.txt"

# === FUNCTIONS ===

# add a sort by ascending and descending order filter

# view individual student record
# allows the user to select a student thenoutput their resutls as per menu item
# how you enable the user to select the student is up to you (either a menu code or by searching the student's name/number)

# show student with the highest and lowest total score
# identify the student with the highest mark and output their results in same format

def displayMenu():
    menu_frame.tkraise()

# make it so that you can add new data/new students with all the required information
# you should also be able to delete records by selecting a student by name or student number to delete their info from the file
# allow the user to be able to select a student by name or student number to update their records - use a sub-menu to edit specific items

# should be able to view all student records 
# def addRow():

# shows the name, number, total coursework mark, exam mark, overall percentage, student grade
# def displayRecords():

# def saveRecords():

# def checkForm():

# def fillForm():

# def clearForm():

# This function calculates the overall percentage into a letter rank or grade
def calculateGrade(percent):
    if percent >= 70:
        return "A"
    if percent >= 60:
        return "B"
    if percent >= 50:
        return "C"
    if percent >= 40:
        return "D"
    else:
        return "F"

# def newRecord():

# def updateRecord():

# def deleteRecord():

# number of students in the class and class average
# def updateClass():
    
# === MAIN MENU FRAME ===

main_frame = Frame(root, bg=BG)

menu_label = Label(menu_frame, text="Student Management System", font=("Georgia", 12), bg=BG, fg="black")
menu_label.pack(pady=10)
count_label = Label(main_frame, text=" Students in Class: 0")
count_label.pack(pady=10)

menu_frame.place(x=0,  y=0, width=850, height=490)

# == (LEFT) FORM FRAME ==

# data is separated into number of students, student code (between 1000 and 9999), three course marks (out of 20), and examination mark (out of 100)

form_frame = Frame(main_frame, bg=BG)

form_label = Label(menu_frame, text="Student Details", font=("Georgia", 12), bg=BG, fg="black")
form_label.grid(row=0, column=0, columnspan=2, pady=10)

add_button = Button(form_frame, text="Add Student", command=)

update_button = Button(form_frame, text="Update Selected", command=)

delete_button = Button(form_frame, text="Delete Selected")

clear_button = Button(form_frame, text="Clear Form")

form_frame.pack(x=0)

# == (RIGHT) TABLE FRAME ==

table_Frame = Frame(main_frame, bg=BG)

table_frame.pack

# === END SETUP ===

displayRecords()
root.mainloop()
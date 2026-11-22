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

student_name = StringVar()
student_num = StringVar()
course1 = StringVar()
course2 = StringVar()
course3 = StringVar()
exam = StringVar()

# === FUNCTIONS ===

# NEED TO MAKE:
# add a sort by ascending and descending order filter
# how you enable the user to select the student is up to you (either a menu code or by searching the student's name/number)
# show student with the highest and lowest total score
# identify the student with the highest mark and output their results in same format

# view individual student record
def displayMenu():
    main_frame.tkraise()

# allow the user to be able to select a student by name or student number to update their records - use a sub-menu to edit specific items

# should be able to view all student records
def addRow(name, num, marks, exam_mark, row_id=None):
    coursework_total = sum(marks)
    percent = (coursework_total + exam_mark) / 160 * 100
    grade = calculateGrade(percent)

    values = (name, num, coursework_total, exam_mark, f"{percent:.1f}%", grade, marks[0], marks[1], marks[2])

    if row_id is None:
        table.insert("", END, values=values)
    else:
        table.item(row_id, values=values)

# shows the name, number, total coursework  mark, exam mark, overall percentage, student grade
def displayRecords():
    with open("Assessment 1 - Skills Portfolio\Exercise 3\studentMarks.txt", "r") as f:
        lines = f.read().splitlines()

    for line in lines[1:]:
        if line.strip() == "":
            continue
        parts = line.split(",")
        try:
            num = int(parts[0])
            name = parts[1]
            marks = [int(parts[2]), int(parts[3]), int(parts[4])]
            exam_mark = int(parts[5])
        except (ValueError, IndexError):
            continue

        addRow(name, num, marks, exam_mark)
    
    # updateClass()

def saveRecords():
    rows = table.get_children()

    with open("Assessment 1 - Skills Portfolio\Exercise 3\studentMarks.txt", "w") as f:
        file.write(str(len(rows)) + "\n")
        for row_id in rows:
            v = table.item(row_id)["values"]
            f.write(f"{v[1]},{v[0]},{v[6]},{v[7]},{v[8]},{v[3]}\n")

def clickTable(event):
    if table.identify_region(event.x, event.y) in ("heading", "separator"):
        return

    row = table.identify_row(event.y)

    if row == "" or row in table.selection():
        clearForm()
        return "break"

def fillForm(event=None):
    selected = table.selection()
    if not selected:
        return
    
    v = table.item(selected[0])["values"]
    student_name.set(v[0])
    student_num.set(v[1])
    course1.set(v[6])
    course2.set(v[7])
    course3.set(v[8])
    exam.set(v[3])

def clearForm():
    table.selection_remove(table.selection())
    student_name.set("")
    student_num.set("")
    course1.set("")
    course2.set("")
    course3.set("")
    exam.set("")

def checkForm(ignore_row=None):
    name = student_name.get().strip()
    num = student_num.get().strip()

    # checks name
    if name == "":
        messagebox.showerror("Error", "Please enter the student's name.")
        return

    # checks if number is valid
    if not num.isdigit() or not (1000 <= int(num) <= 9999):
        messagebox.showerror("Error", "Student number must be between 1000 and 9999.")
        return
    
    # checks if number already exists
    for row_id in table.get_children():
        if row_id == ignore_row:
            continue
        if table.item(row_id)["values"][1] == int(num):
            messagebox.showerror("Error", "That student number already exists.")
            return
    
    # checks marks are numbers
    try:
        marks = [int(course1.get()), int(course2.get()), int(course3.get())]
        exam_mark = int(exam.get())
    except ValueError:
        messagebox.showerror("Error", "Marks must be whole numbers.")
        return

    # checks marks are in the range given
    for m in marks:
        if m < 0 or m > 20:
            messagebox.showerror("Error", "Each course mark must be between 0 and 20.")
            return
    if exam_mark < 0 or exam_mark > 100:
        messagebox.showerror("Error", "Exam mark must be between 0 and 100.")
        return
    
    # if all passes the checks, use the values
    return name, int(num), marks, exam_mark

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

# make it so that you can add new data/new students with all the required information
def newRecord():
    result = checkForm()
    if result is None:
        return

    name, num, marks, exam_mark = result
    addRow(name, num, marks, exam_mark)

# allows the user to select a student thenoutput their resutls as per menu item
def updateRecord():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Nothing selected", "Click a student in the table first.")
        return

    row_id = selected[0]

    result = checkForm(ignore_row=row_id)
    if result is None:
        return
    
    name, num, marks, exam_mark = result

    addRow(name, num, marks, exam_mark, row_id)

    saveRecords()
    messagebox.showinfo("Updated", "Student details updated.")

# you should also be able to delete records by selecting a student by name or student number to delete their info from the file
def deleteRecord():
    selected = table.selection()

    if not selected:
        messagebox.showwarning("Nothing selected", "Click a student in the table first.")
        return

    if messagebox.askyesno("Confirm", "Delete the selected student?"):
        for row_id in selected:
            table.delete(row_id)
        saveRecords()

# number of students in the class and class average
def updateClass():
    rows = table.get_children()
    count = len(rows)

    if count == 0:
        average_text = "-"
    else:
        total_percent = 0
        for row_id in rows:
            v = table.item(row_id)["values"]
            total_percent += (v[2] + v[3]) / 160 * 100
        average_text = f"{total_percent / count:.1f}%"
    
    count_label.config(text=f"Students in Class: {count}      Class Average: {average_text}")
    
# === MAIN MENU FRAME ===

main_frame = Frame(root, bg=BG)

menu_label = Label(main_frame, text="Student Management System", font=("Georgia", 12), bg=BG, fg="black")
menu_label.pack(pady=10)
count_label = Label(main_frame, text="Students in Class: 0      Class Average: -", font=("Georgia", 12), bg=BG, fg="black")
count_label.pack(side=BOTTOM, anchor=W, padx=20, pady=(0, 10))

main_frame.place(x=0,  y=0, width=850, height=490)

# == (LEFT) FORM FRAME ==

# data is separated into number of students, student code (between 1000 and 9999), three course marks (out of 20), and examination mark (out of 100)
form_frame = Frame(main_frame, bg=BG)

form_label = Label(form_frame, text="Student Details", font=("Georgia", 12), bg=BG, fg="black")
form_label.grid(row=0, column=0, columnspan=2, pady=10)

fields = [
    ("Name", student_name),
    ("Student Number", student_num),
    ("Course 1 (/20)", course1),
    ("Course 2 (/20)", course2),
    ("Course 3 (/20)", course3),
    ("Exam (/100)", exam),
]

for i, (text, var) in enumerate(fields, start=1):
    Label(form_frame, text=text, font=("Georgia", 10), bg=BG, fg="black").grid(row=i, column=0, sticky=W, pady=4)
    Entry(form_frame, textvariable=var, width=18).grid(row=i, column=1, pady=4, padx=5)
    
add_button = Button(form_frame, text="Add Student", width=20, command=newRecord)
add_button.grid(row=7, column=0, columnspan=2, pady=(15, 4))

update_button = Button(form_frame, text="Update Selected", width=20, command=updateRecord)
update_button.grid(row=8, column=0, columnspan=2, pady=4)

delete_button = Button(form_frame, text="Delete Selected", width=20, command=deleteRecord)
delete_button.grid(row=9, column=0, columnspan=2, pady=4)

clear_button = Button(form_frame, text="Clear Form", width=20, command=clearForm)
clear_button.grid(row=10, column=0, columnspan=2, pady=4)

form_frame.pack(side=LEFT, anchor=N, padx=20, pady=10)

# == (RIGHT) TABLE FRAME ==

table_frame = Frame(main_frame, bg=BG)

tree_frame = Frame(table_frame, bg=BG)
tree_frame.pack(side=TOP, fill=BOTH, expand=True)

columns = ("Name", "Number", "Coursework", "Exam", "Percent", "Grade")
hidden_columns = ("C1", "C2", "C3")

table = ttk.Treeview(tree_frame, columns=columns + hidden_columns, displaycolumns=columns, show="headings", height=11)
widths = {"Name": 140, "Number": 70, "Coursework": 90, "Exam" :60, "Percent": 80, "Grade": 50}
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=widths[col], anchor=CENTER)

scrollbar = Scrollbar(tree_frame, orient=VERTICAL, command=table.yview)
table.config(yscrollcommand=scrollbar.set)

table.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

table.bind("<<TreeviewSelect>>", fillForm)
table.bind("<Button-1>", clickTable)

table_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=10)

# === END SETUP ===

displayRecords()
root.mainloop()
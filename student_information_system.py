
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Student Information System")

# Load and display the image in the left corner
photo = tk.PhotoImage(file="D:\Advanced Programming\wrld.png")
label_image = tk.Label(root, image=photo)
label_image.config(width=200, height=200)
label_image.grid(row=0, column=0, rowspan=8, padx=10, pady=10, sticky="nw")

# Initialize an empty list to store student records
student_list = []

# Function to add a student
def add_student():
    name = entry_name.get()
    roll_number = entry_roll_number.get()
    course = entry_course.get()
    marks = entry_marks.get()
    grading = entry_grading.get()

    if name == "" or roll_number == "" or course == "" or marks == "" or grading == "":
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Input Error", "Marks should be a number.")
        return

    student = {
        "name": name,
        "roll_number": roll_number,
        "course": course,
        "marks": marks,
        "grading": grading
    }

    student_list.append(student)
    display_student_list()
    clear_entries()

# Function to display student information in the listbox
def display_student_list():
    listbox_students.delete(0, tk.END)
    for student in student_list:
        listbox_students.insert(tk.END, f"{student['name']} - {student['roll_number']} - {student['course']} - {student['marks']} - {student['grading']}")
# update the stu list
def update_student():
    try:
        # Get the selected student's index
        selected_student_index = listbox_students.curselection()[0]
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a student to update.")
        return

    name = entry_name.get()
    roll_number = entry_roll_number.get()
    course = entry_course.get()
    marks = entry_marks.get()
    grading = entry_grading.get()

    # Check for empty fields
    if name == "" or roll_number == "" or course == "" or marks == "" or grading == "":
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # Validate marks as a number
    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Input Error", "Marks should be a number.")
        return

    # Update the student data
    student_list[selected_student_index] = {
        "name": name,
        "roll_number": roll_number,
        "course": course,
        "marks": marks,
        "grading": grading
    }

    # Update the listbox to reflect changes
    display_student_list()
    clear_entries()
    messagebox.showinfo("Success", "Student data updated successfully.")

def prefill_entries(event):
    try:
        selected_student_index = listbox_students.curselection()[0]
        student = student_list[selected_student_index]

        entry_name.delete(0, tk.END)
        entry_name.insert(0, student["name"])
        entry_roll_number.delete(0, tk.END)
        entry_roll_number.insert(0, student["roll_number"])
        entry_course.delete(0, tk.END)
        entry_course.insert(0, student["course"])
        entry_marks.delete(0, tk.END)
        entry_marks.insert(0, student["marks"])
        entry_grading.delete(0, tk.END)
        entry_grading.insert(0, student["grading"])
    except IndexError:
        pass
    
listbox_students = tk.Listbox(root, width=80, height=10)
listbox_students.grid(row=8, column=1, columnspan=3, padx=10, pady=5)
listbox_students.bind("<<ListboxSelect>>", prefill_entries)

    
# Function to clear the entry fields after adding a student
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_roll_number.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_marks.delete(0, tk.END)
    entry_grading.delete(0, tk.END)

# Function to delete a selected student record
def delete_student():
    try:
        selected_student_index = listbox_students.curselection()[0]
        del student_list[selected_student_index]
        display_student_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a student to delete.")

# Labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=1, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=2, padx=10, pady=5)

label_roll_number = tk.Label(root, text="Roll Number:")
label_roll_number.grid(row=1, column=1, padx=10, pady=5)
entry_roll_number = tk.Entry(root)
entry_roll_number.grid(row=1, column=2, padx=10, pady=5)

label_course = tk.Label(root, text="Course:")
label_course.grid(row=2, column=1, padx=10, pady=5)
entry_course = tk.Entry(root)
entry_course.grid(row=2, column=2, padx=10, pady=5)

label_marks = tk.Label(root, text="Marks:")
label_marks.grid(row=3, column=1, padx=10, pady=5)
entry_marks = tk.Entry(root)
entry_marks.grid(row=3, column=2, padx=10, pady=5)

label_grading = tk.Label(root, text="Grading:")
label_grading.grid(row=4, column=1, padx=10, pady=5)
entry_grading = tk.Entry(root)
entry_grading.grid(row=4, column=2, padx=10, pady=5)

# Buttons for adding and deleting students
button_add = tk.Button(root, text="Add Student", command=add_student)
button_add.grid(row=5, column=1, padx=10, pady=10)

button_update = tk.Button(root, text="Update Student", command=update_student)
button_update.grid(row=5, column=2, padx=10, pady=10)

button_delete = tk.Button(root, text="Delete Selected Student", command=delete_student)
button_delete.grid(row=5, column=3, padx=10, pady=10)

# Listbox to display students
label_student_list = tk.Label(root, text="Student List:")
label_student_list.grid(row=7, column=1, columnspan=3, padx=10, pady=5)

listbox_students = tk.Listbox(root, width=80, height=10)
listbox_students.grid(row=8, column=1, columnspan=3, padx=10, pady=5)


root.mainloop()

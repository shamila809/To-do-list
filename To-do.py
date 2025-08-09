from tkinter import *
from tkinter import messagebox
import os

# Main application window
root = Tk()
root.title("To-Do List App")
root.geometry("400x450")

# File to store tasks
FILE_NAME = "tasks.txt"

# List to store tasks during app runtime
tasks = []

# Function to update the listbox display
def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

# Add new task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, END)

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)  # Remove task by index instead of name
        update_listbox()

# Save tasks to file when Save button is clicked
def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks have been saved successfully!")


# Load tasks from file when app starts
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                tasks.append(line.strip())
        update_listbox()

# Toggle ✔ mark for completed/uncompleted tasks
def mark_completed(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        if task.startswith("✔ "):
            tasks[index] = task[2:]
        else:
            tasks[index] = "✔ " + task
        update_listbox()

# GUI layout
frame = Frame(root)
frame.pack(pady=10)

listbox = Listbox(frame, width=35, height=10, font=("Arial", 14))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

add_button = Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

save_button = Button(root, text="Save Tasks", width=20, command=save_tasks)
save_button.pack(pady=5)

# Bind click to mark completed
listbox.bind('<Double-Button-1>', mark_completed)


# Load tasks when app starts
load_tasks()

# Start GUI
root.mainloop()

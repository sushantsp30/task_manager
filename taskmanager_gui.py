import sys
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    update_task_list()

def delete_task(task_index):
    try:
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def view_tasks():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        task_list.insert(tk.END, f'{i + 1}. {task["task"]} [{status}]')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def update_task_list():
    view_tasks()

def add_task_command():
    task = task_entry.get()
    if task:
        add_task(task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def delete_task_command():
    try:
        task_index = int(task_entry.get()) - 1
        delete_task(task_index)
        task_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid task number")

def complete_task_command():
    try:
        task_index = int(task_entry.get()) - 1
        mark_task_completed(task_index)
        task_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid task number")

def main():
    global task_entry, task_list

    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("600x400")
    root.configure(bg="#f0f0f0")

    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=10)

    task_entry = tk.Entry(frame, width=50, font=("Helvetica", 14))
    task_entry.pack(side=tk.LEFT, padx=10)

    add_button = tk.Button(frame, text="Add Task", command=add_task_command, bg="#4CAF50", fg="white", font=("Helvetica", 12))
    add_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(frame, text="Delete Task", command=delete_task_command, bg="#f44336", fg="white", font=("Helvetica", 12))
    delete_button.pack(side=tk.LEFT, padx=5)

    complete_button = tk.Button(frame, text="Complete Task", command=complete_task_command, bg="#2196F3", fg="white", font=("Helvetica", 12))
    complete_button.pack(side=tk.LEFT, padx=5)

    task_list = tk.Listbox(root, width=80, height=20, font=("Helvetica", 12), bg="#ffffff", fg="#000000", selectbackground="#cce7ff")
    task_list.pack(pady=10)

    view_tasks()

    root.mainloop()

if __name__ == "__main__":
    main()

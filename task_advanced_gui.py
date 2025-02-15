import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

def add_task(task, start_date, end_date):
    tasks.append({
        "task": task,
        "completed": False,
        "start_date": start_date,
        "end_date": end_date
    })
    update_task_list()

def delete_task(task_index):
    try:
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def view_tasks():
    task_list.delete(0, tk.END)
    current_date = datetime.now().date()
    for i, task in enumerate(tasks):
        end_date = datetime.strptime(task["end_date"], "%Y-%m-%d").date()
        if current_date > end_date:
            task["completed"] = True
        status = "Completed" if task["completed"] else "Pending"
        task_list.insert(tk.END, f'{i + 1}. {task["task"]} [{status}] (Start: {task["start_date"]}, End: {task["end_date"]})')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def update_task_list():
    view_tasks()

def add_task_gui():
    task = task_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
        add_task(task, start_date, end_date)
        task_entry.delete(0, tk.END)
        start_date_entry.delete(0, tk.END)
        end_date_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")

def delete_task_gui():
    selected_task = task_list.curselection()
    if selected_task:
        delete_task(selected_task[0])
    else:
        messagebox.showerror("Error", "No task selected")

def mark_task_completed_gui():
    selected_task = task_list.curselection()
    if selected_task:
        mark_task_completed(selected_task[0])
    else:
        messagebox.showerror("Error", "No task selected")

app = tk.Tk()
app.title("Task Manager")
app.configure(bg="#f0f0f0")

frame = tk.Frame(app, bg="#f0f0f0")
frame.pack(pady=10)

task_label = tk.Label(frame, text="Task:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
task_label.grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(frame, width=50, font=("Arial", 12))
task_entry.grid(row=0, column=1, padx=5, pady=5)

start_date_label = tk.Label(frame, text="Start Date (YYYY-MM-DD):", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
start_date_label.grid(row=1, column=0, padx=5, pady=5)
start_date_entry = tk.Entry(frame, width=20, font=("Arial", 12))
start_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

end_date_label = tk.Label(frame, text="End Date (YYYY-MM-DD):", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
end_date_label.grid(row=2, column=0, padx=5, pady=5)
end_date_entry = tk.Entry(frame, width=20, font=("Arial", 12))
end_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

add_button = tk.Button(frame, text="Add Task", command=add_task_gui, bg="#4CAF50", fg="white", font=("Arial", 12))
add_button.grid(row=3, column=0, columnspan=2, pady=10)

task_list = tk.Listbox(app, width=80, height=10, font=("Arial", 12), bg="#ffffff", fg="#333333", selectbackground="#4CAF50", selectforeground="white")
task_list.pack(pady=10)

button_frame = tk.Frame(app, bg="#f0f0f0")
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task_gui, bg="#f44336", fg="white", font=("Arial", 12))
delete_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(button_frame, text="Mark as Completed", command=mark_task_completed_gui, bg="#2196F3", fg="white", font=("Arial", 12))
complete_button.grid(row=0, column=1, padx=5)

view_tasks()

app.mainloop()

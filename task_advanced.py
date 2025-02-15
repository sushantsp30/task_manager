import sys
from datetime import datetime

tasks = []

def add_task(task, start_date, end_date, due_date, priority):
    tasks.append({
        "task": task,
        "completed": False,
        "start_date": start_date,
        "end_date": end_date,
        "due_date": due_date,
        "priority": priority
    })
    print(f'Added task: {task} (Start: {start_date}, End: {end_date}, Due: {due_date}, Priority: {priority})')

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(f'Deleted task: {removed_task["task"]}')
    except IndexError:
        print("Invalid task number")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        current_date = datetime.now().date()
        for i, task in enumerate(tasks):
            end_date = datetime.strptime(task["end_date"], "%Y-%m-%d").date()
            if current_date > end_date:
                task["completed"] = True
            status = "Completed" if task["completed"] else "Pending"
def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        print(f'Marked task as completed: {tasks[task_index]["task"]}')
    except IndexError:
        print("Invalid task number")

def show_help():
    print("""
    Available commands:
    - add <task> <start_date> <end_date>: Add a new task with start and end dates (format: YYYY-MM-DD)
    - delete <task_number>: Delete a task by its number
    - view: View all tasks
    - complete <task_number>: Mark a task as completed
    - help: Show this help message
    - exit: Exit the application
    """)

def main():
    print("Task Manager Application")
    show_help()
    while True:
        command = input("Enter command: ").strip().split()
        if not command:
            continue
        if command[0] == "add":
            if len(command) >= 4:
                task = " ".join(command[1:-2])
                start_date = command[-2]
                end_date = command[-1]
                try:
                    datetime.strptime(start_date, "%Y-%m-%d")
                    datetime.strptime(end_date, "%Y-%m-%d")
                    add_task(task, start_date, end_date)
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD.")
            else:
                print("Invalid command. Usage: add <task> <start_date> <end_date>")
        elif command[0] == "delete":
            if len(command) > 1 and command[1].isdigit():
                delete_task(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif command[0] == "view":
            view_tasks()
        elif command[0] == "complete":
            if len(command) > 1 and command[1].isdigit():
                mark_task_completed(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif command[0] == "help":
            show_help()
        elif command[0] == "exit":
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()

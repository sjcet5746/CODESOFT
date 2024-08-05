#1.A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists
import json

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"id": len(tasks) + 1, "task": task, "status": "Pending"})
    print("Task added!")

def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = input("Enter new task description: ")
            task['status'] = input("Enter new status (Pending/Completed): ")
            print("Task updated!")
            return
    print("Task not found!")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    print("Task deleted!")

def view_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Update Task\n3. Delete Task\n4. View Tasks\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
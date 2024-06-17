import json
import os

# Initialize an empty list for tasks
tasks = []

# Function to add a task
def add_task(description):
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'pending'
    }
    tasks.append(task)
    print(f"Task added: {task}")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"{task['id']}. {task['description']} - {task['status']}")

# Function to update a task
def update_task(task_id, description=None, status=None):
    for task in tasks:
        if task['id'] == task_id:
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            print(f"Task updated: {task}")
            return
    print(f"Task with id {task_id} not found.")

# Function to delete a task
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task with id {task_id} deleted.")

# Function to save tasks to a file
def save_tasks(filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved.")

# Function to load tasks from a file
def load_tasks(filename="tasks.json"):
    global tasks
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded.")
    else:
        print("No saved tasks found.")

# Main function to run the application
def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description (leave blank to keep current): ")
            status = input("Enter new status (pending/done, leave blank to keep current): ")
            update_task(task_id, description or None, status or None)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            save_tasks()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display tasks in a formatted manner."""
    print("\n=== To-Do List ===")
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else "✗"
        print(f"{idx}. [{status}] {task['title']} - {task['description']}")
    print()

def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    tasks.append({"title": title, "description": description, "completed": False})
    print("Task added successfully!")

def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['title'] = input("New task title: ").strip() or tasks[task_num]['title']
        tasks[task_num]['description'] = input("New task description: ").strip() or tasks[task_num]['description']
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def mark_complete(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['completed'] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number!")

def main():
    """Main function to run the To-Do List app."""
    tasks = load_tasks()

    while True:
        print("\nOptions: 1. View 2. Add 3. Update 4. Delete 5. Mark Complete 6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_complete(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

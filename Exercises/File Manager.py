def display_menu():
    print("Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Quit")

def add_task(tasks, task_id_counter):
    description = input("Enter the task description: ")
    priority = input("Enter the task priority (low, medium, high): ").lower()
    tasks[task_id_counter] = {"description": description, "priority": priority, "completed": False}
    print(f"Task {task_id_counter} added.")
    return task_id_counter + 1

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"ID: {task_id}, Description: {task['description']}, Priority: {task['priority']}, Status: {status}")

def mark_task_completed(tasks):
    task_id = int(input("Enter the ID of the task to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print(f"Task {task_id} marked as completed.")
    else:
        print("Task ID not found.")

def delete_task(tasks):
    task_id = int(input("Enter the ID of the task to delete: "))
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print("Task ID not found.")

def main():
    tasks = {}
    task_id_counter = 1
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task_id_counter = add_task(tasks, task_id_counter)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()

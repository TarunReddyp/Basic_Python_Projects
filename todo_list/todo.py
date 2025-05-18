import json
import os
filepath ="D:\\Basic_python_projects\\todo_list\\todo_list.json"
def load_tasks():
   
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try: 
                tasks = json.load(f)
                return tasks
            except json.JSONDecodeError:
                print("Error: Could not decode the to-do list file. Starting with an empty list.")
                return []
    return []
def save_tasks(tasks):
   
    with open(filepath, 'w') as f:
        json.dump(tasks,f)
        print("To-do list saved.")

def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else :
        print("--- Tasks ---")
        for index, task in enumerate(tasks):
            status = "[X]" if task.get('complete', False) else "[ ]"
            print(f"{index + 1}. {status} {task['description']}")

def add_task(tasks):
    description = input("Enter the task: ")
    tasks.append({'description': description, 'complete': False})
    print(f"Task '{description}' added.")

def find_task_by_name(tasks,search_term):
    found_indices = []
    for index, task in enumerate(tasks):
        if search_term.lower() in task['description'].lower():
            found_indices.append(index)
    return found_indices

def mark_complete(tasks):
    if not tasks:
        print(" Your to-do list is empty.")
        return
    search_term = input("Enter the name (or part of the name) of the task to mark as complete: ")
    found_indices = find_task_by_name(tasks, search_term)
    if not found_indices:
        print(f"No tasks found matching '{search_term}'.")
    elif len(found_indices) == 1:
        task_index = found_indices[0]
        tasks[task_index]['complete'] = True
        print(f"Task '{tasks[task_index]['description']}' marked as complete.")
    else:
        print("Multiple tasks found:")
        for index in found_indices:
            status = "[X]" if tasks[index].get('complete', False) else "[ ]"
            print(f"{index + 1}. {status} {tasks[index]['description']}")
        try:
            task_number = int(input("Enter the number of the task to mark as complete: ")) - 1
            if 0 <= task_number < len(found_indices):
                task_index = found_indices[task_number]
                tasks[task_index]['complete'] = True
                print(f"Task '{tasks[task_index]['description']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def edit_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    search_term = input("Enter the name (or part of the name) of the task to edit: ")
    found_indices = find_task_by_name(tasks, search_term)
    if not found_indices:
        print(f"No tasks found matching '{search_term}'.")
    elif len(found_indices) == 1:
        task_index = found_indices[0]
        new_description = input("Enter the new description for the task: ")
        tasks[task_index]['description'] = new_description
        print(f"Task updated to '{new_description}'.")
    else:
        print("Multiple tasks found:")
        for index in found_indices:
            status = "[X]" if tasks[index].get('complete', False) else "[ ]"
            print(f"{index + 1}. {status} {tasks[index]['description']}")
        try:
            task_number = int(input("Enter the number of the task to edit: ")) - 1
            if 0 <= task_number < len(found_indices):
                task_index = found_indices[task_number]
                new_description = input("Enter the new description for the task: ")
                tasks[task_index]['description'] = new_description
                print(f"Task updated to '{new_description}'.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def remove_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    search_term = input("Enter the name (or part of the name) of the task to remove: ")
    found_indices = find_task_by_name(tasks, search_term)
    if not found_indices:
        print(f"No tasks found matching '{search_term}'.")
    elif len(found_indices) == 1:
        task_index = found_indices[0]
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['description']}' removed.")
    else:
        print("Multiple tasks found:")
        for index in found_indices:
            status = "[X]" if tasks[index].get('complete', False) else "[ ]"
            print(f"{index + 1}. {status} {tasks[index]['description']}")
        try:
            task_number = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= task_number < len(found_indices):
                task_index = found_indices[task_number]
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task['description']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def todo_list():
    tasks = load_tasks()

    while True:
        print("\n--- Enhanced To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Edit task")
        print("5. Remove task")
        print("6. Save and Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            remove_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    todo_list()
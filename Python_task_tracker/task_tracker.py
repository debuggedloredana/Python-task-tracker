import json
import os

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

else:
    tasks = []


def add_task():
    new_task = input("Please add a new task: ")
    task = {
        "title": new_task,
        "completed": False
    }
    tasks.append(task)

    save_tasks()
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("You have no tasks to view yet.")
    else:
        for number, task in enumerate(tasks, start=1):
            if task["completed"] == True:
                print(f"{number}. {task["title"]} - Completed")
            else:
                print(f"{number}. {task["title"]} - Outstanding")

def complete_task():
    if not tasks:
        print("You have no tasks to complete yet.")
        return
    view_tasks()
    try: 
        task_number = int(input("Which task number would you like to mark as complete? "))
        task_index = task_number - 1
            
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
                
            save_tasks()
            print("Task marked as complete!")
            
        else:
            print("Invalid task number.")
        
    except ValueError:
            print("Please enter a valid number.")

def delete_task():
    if not tasks:
        print("You have no tasks to delete yet.")
        return
    view_tasks()
    try:
            deleted_task = int(input("Which task number would you like to delete? "))
            task_index = deleted_task - 1
        
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                save_tasks()
                print("Task deleted successfully!")
            
            else:
                print("Invalid task number.")

    except ValueError:
            print("Please enter a valid number. ")
            

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

while True:
    print("\n===========MY TASK TRACKER===========")
    print("\n Welcome! What would you like to do?")
    print("\n1. View tasks")
    print("\n2. Add a task")
    print("\n3. Mark a task as complete")
    print("\n4. Delete a task")
    print("\n5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice... please try again.")

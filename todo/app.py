import json
# load existing items
# create new item
# list item 
# mark item as complete 
# save items


file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except: 
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            return json.dump(tasks, file)
    except: 
        print("Failed to save")

def view_tasks(tasks):
    task_list = tasks["tasks"] 
    if len(task_list) == 0:
        print("No tasks to display")
    else:
        print("Your To-Do List: ")
        print()

        for index, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{index + 1} . {task['description']} | {status}")

def create_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description" : description, "complete" : False})
        save_tasks(tasks)
    else:
        print("Description can not be empty")
    
    print("Task added.")

def mark_task_complete(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Which task do you want to mark as completed: ").strip())

        task_list = tasks["tasks"]

        if 1 <= task_number <= len(task_list):
            task_list[task_number - 1]['complete'] = True
            save_tasks(tasks)
            print("Task marked as successful")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid task number")


def main():

    tasks = load_tasks()
    # print("loaded", tasks)

    while True:
        print("\n Todo List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exist Task")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid Choice. Please try again.")
            break

main()
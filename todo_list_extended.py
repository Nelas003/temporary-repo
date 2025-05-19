todo_list = []

while True:
    command = input("\nType 'add' to add a task, 'view' to see tasks, or 'quit' to exit: ")

    if command == "quit":
        print("Thank you for using the To-Do List!")
        break

    elif command == "view":
        if not todo_list:
            print("No tasks yet.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task['description']} (Date: {task['date']})")

    elif command == "add":
        description = input("Enter task description: ")
        date = input("Enter due date (e.g. 2025-06-01): ")
        todo_list.append({"description": description, "date": date})
        print("\nTask added. Current To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task['description']} (Date: {task['date']})")

    else:
        print("Invalid command. Please type 'add', 'view', or 'quit'.")

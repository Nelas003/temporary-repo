todo_list = []

while True:
    command = input("Type a task, 'view' to see tasks, or 'quit' to exit: ")

    if command == "quit":
        print("Thank you for using the To-Do List!")
        break
    elif command == "view":
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        todo_list.append(command)
        print("Task added.")
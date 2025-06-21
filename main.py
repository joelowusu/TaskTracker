from task_manager import TaskManager

# Shows the menu options
def print_menu():
    print("\nTaskTrack - Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as complete")
    print("5. Exit")

# Main function - runs the program
def main():
    # Load tasks from the file
    manager = TaskManager("tasks.json")

    while True:
        print_menu()
        choice = input("Enter choice: ")

        # Add task
        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            manager.add_task(title, desc)
            print("Task added!")

        # View tasks
        elif choice == "2":
            tasks = manager.list_tasks()
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.title} [{task.status}] - {task.description}")

        # Delete task
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)
            print("Task deleted.")

        # Mark task as complete
        elif choice == "4":
            index = int(input("Enter task number to mark complete: ")) - 1
            manager.mark_complete(index)
            print("Task marked as complete.")

        # Exit
        elif choice == "5":
            break

        else:
            print("Invalid choice.")

# Runs the program
if __name__ == "__main__":
    main()


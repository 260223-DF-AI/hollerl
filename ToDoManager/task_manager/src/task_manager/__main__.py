"""Entry point for the task manager CLI."""

from task_manager.models.task import Task
from task_manager.utils.formatters import format_task_list, format_task_detail
from task_manager.utils.validators import validate_title, ValidationError


def print_welcome():
    """Print welcome message."""
    print("=" * 40)
    print("       TASK MANAGER CLI v1.0")
    print("=" * 40)
    print()


def print_menu():
    """Print the main menu."""
    print("\nOptions:")
    print("  1. Add a task")
    print("  2. List all tasks")
    print("  3. Mark task complete")
    print("  4. Delete a task")
    print("  5. Exit")
    print()


def main():
    """Main function to run the CLI."""
    tasks = []
    
    print_welcome()
    
    while True:
        print_menu()
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == "1":
            # Add task
            try:
                title = input("Enter task title: ")
                title = validate_title(title)
                description = input("Enter description (optional): ")
                task = Task(title, description)
                tasks.append(task)
                print(f"\nTask #{task.id} created successfully!")
            except ValidationError as e:
                print(f"\nError: {e}")
        
        elif choice == "2":
            # List tasks
            print("\n" + format_task_list(tasks))
        
        elif choice == "3":
            # Mark complete
            if not tasks:
                print("\nNo tasks to complete.")
                continue
            try:
                task_id = int(input("Enter task ID to complete: "))
                task = next((t for t in tasks if t.id == task_id), None)
                if task:
                    task.mark_complete()
                    print(f"\nTask #{task_id} marked complete!")
                else:
                    print(f"\nTask #{task_id} not found.")
            except ValueError:
                print("\nPlease enter a valid number.")
        
        elif choice == "4":
            # Delete task
            if not tasks:
                print("\nNo tasks to delete.")
                continue
            try:
                task_id = int(input("Enter task ID to delete: "))
                task = next((t for t in tasks if t.id == task_id), None)
                if task:
                    tasks.remove(task)
                    print(f"\nTask #{task_id} deleted!")
                else:
                    print(f"\nTask #{task_id} not found.")
            except ValueError:
                print("\nPlease enter a valid number.")
        
        elif choice == "5":
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
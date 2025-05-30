# main.py

from habit_manager import add_habit, mark_habit_completed, generate_weekly_report, delete_habit, list_habits

def show_menu():
    print("\nSimple Habit Tracker")
    print("====================")
    print("1. Add a new habit")
    print("2. Mark habit as completed")
    print("3. View weekly report")
    print("4. Delete a habit")
    print("5. List all habits")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            habit_name = input("Enter the name of the habit: ").strip()
            add_habit(habit_name)

        elif choice == "2":
            habit_name = input("Enter the name of the habit to mark complete: ").strip()
            mark_habit_completed(habit_name)
        
        elif choice == "3":
            generate_weekly_report()
        
        elif choice == "4":
            habit_name = input("Enter the name of the habit to delete: ").strip()
            delete_habit(habit_name)
        
        elif choice == "5":
            list_habits()

        elif choice == "6":
            print("Exiting Habit Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

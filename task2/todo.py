from pathlib import Path
TASK_FILE = Path(__file__).parent / "tasks.txt"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def load_tasks():
    tasks = {day: [] for day in DAYS}
    try:
        with open(TASK_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(" | ")
                if len(parts) != 3:
                    continue  
                day, task_text, status = parts
                if day in DAYS:
                    tasks[day].append({"task": task_text, "status": status})
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for day in DAYS:
            for t in tasks[day]:
                f.write(f"{day} | {t['task']} | {t['status']}\n")

def show_menu():
    print("\n--- Weekly To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Edit task")
    print("6. Remove all task at once ")
    print("7. Mark all tasks as done")
    print("8. Exit")

def choose_day():
    print("Select a day:")
    for i, day in enumerate(DAYS, start=1):
        print(f"{i}. {day}")
    while True:
        try:
            num = int(input("Enter day number: "))
            if 1 <= num <= 7:
                return DAYS[num - 1]
            print("Invalid number, try again.")
        except ValueError:
            print("Enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":  # View tasks
            for day in DAYS:
                print(f"\n--- {day} ---")
                if not tasks[day]:
                    print("No tasks yet.")
                else:
                    for i, t in enumerate(tasks[day], start=1):
                        status_symbol = "👍" if t["status"] == "Done" else "⏳"
                        print(f"{i}. {t['task']} [{status_symbol}]")

        elif choice == "2":  # Add task
            day = choose_day()
            task_text = input(f"Enter task for {day}: ")
            tasks[day].append({"task": task_text, "status": "Pending"})
            save_tasks(tasks)
            print(f"Task added 👍 for {day}")

        elif choice == "3":  # Mark task as done
            day = choose_day()
            if not tasks[day]:
                print(f"No tasks to mark for {day}.")
                continue
            for i, t in enumerate(tasks[day], start=1):
                print(f"{i}. {t['task']} [{t['status']}]")
            try:
                num = int(input("Enter task number to mark as done: "))
                tasks[day][num-1]["status"] = "Done"
                save_tasks(tasks)
                print(f"Marked as done 👍 -> {tasks[day][num-1]['task']}")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "4":  # Remove task
            day = choose_day()
            if not tasks[day]:
                print(f"No tasks to remove for {day}.")
                continue
            for i, t in enumerate(tasks[day], start=1):
                print(f"{i}. {t['task']} [{t['status']}]")
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks[day].pop(num-1)
                save_tasks(tasks)
                print(f"Removed: {removed['task']} 👍")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "5":  # Edit task
            day = choose_day()
            if not tasks[day]:
                print(f"No tasks to edit for {day}.")
                continue
            for i, t in enumerate(tasks[day], start=1):
                print(f"{i}. {t['task']} [{t['status']}]")
            try:
                num = int(input("Enter task number to edit: "))
                new_text = input("Enter updated task text: ")
                tasks[day][num-1]["task"] = new_text
                save_tasks(tasks)
                print(f"Task updated 👍 -> {new_text}")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "6":  # Remove all tasks
            confirm = input("Are you sure you want to remove ALL tasks? (y/n): ").lower()
            if confirm == "y":
                tasks = {day: [] for day in DAYS}  # clear all tasks
                save_tasks(tasks)                  
                print("All tasks removed 👍")

        elif choice == "7":  # Mark all tasks as done
                confirm = input("Are you sure you want to mark ALL tasks as done? (y/n): ").lower()
                if confirm == "y":
                    for day in DAYS:
                        for task in tasks[day]:
                            task["status"] = "Done"
                    save_tasks(tasks)
                    print("All tasks for the week are now marked as done 👍")


        elif choice == "8":
            print("You're all set to tackle the day—one task at a time. Let’s make it productive and satisfying. Ready when you are!👍")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

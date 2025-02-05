from model import *

# CLI Menu
def main():
    while True:
        print("\n📌 Task Manager")
        print("1️⃣ Add Task")
        print("2️⃣ View All Tasks")
        print("3️⃣ View Pending Tasks")
        print("4️⃣ View Completed Tasks")
        print("5️⃣ Sort Tasks")
        print("6️⃣ Update Task Description")
        print("7️⃣ Update Task Status")
        print("8️⃣ Search Task")
        print("9️⃣ Delete Task")
        print("🔟 View Tasks Due Soon (24 hrs)")
        print("1️⃣1️⃣Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ")
            add_task(description, deadline)

        elif choice == "2":
            tasks = get_all_tasks()
            if not tasks:
                print("No tasks found!\n")
            else:
                print("\n📋 ALL TASKS:")
                for task in tasks:
                    print(f"[{task.id}] {task.description} | Deadline: {task.deadline} | Status: {task.status}")

        elif choice == "3":
            tasks = get_tasks_by_status("Pending")
            if not tasks:
                print("No pending tasks!\n")
            else:
                print("\n📋 PENDING TASKS:")
                for task in tasks:
                    print(f"[{task.id}] {task.description} | Deadline: {task.deadline}")

        elif choice == "4":
            tasks = get_tasks_by_status("Completed")
            if not tasks:
                print("No completed tasks!\n")
            else:
                print("\n📋 COMPLETED TASKS:")
                for task in tasks:
                    print(f"[{task.id}] {task.description} | Deadline: {task.deadline}")

        elif choice == "5":
            sort_option = input("Sort by (deadline/status): ")
            tasks = get_all_tasks(sort_option)
            if not tasks:
                print("No tasks found!\n")
            else:
                print("\n📋 SORTED TASKS:")
                for task in tasks:
                    print(f"[{task.id}] {task.description} | Deadline: {task.deadline} | Status: {task.status}")


        elif choice == "6":
            task_id = input("Enter task ID to update description: ")
            new_description = input("Enter new description: ")
            update_task_description(task_id, new_description)

        elif choice == "7":
            task_id = input("Enter task ID to update status: ")
            new_status = input("Enter new status (Pending/Completed): ")
            update_task_status(task_id, new_status)


        elif choice == "8":

            keyword = input("Enter a keyword to search for tasks: ")

            tasks = search_tasks(keyword)

            if not tasks:

                print("No matching tasks found!\n")

            else:

                print("\n🔍 SEARCH RESULTS:")

                for task in tasks:
                    print(f"[{task.id}] {task.description} | Deadline: {task.deadline} | Status: {task.status}")

        elif choice == "9":
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)

        elif choice == "10":
            tasks = get_due_soon_tasks()
            if not tasks:
                print("No tasks due within 24 hours!\n")
            else:
                print("\n🔔 TASKS DUE SOON:")
                for task in tasks:
                    print(f"[{task.id}] {task.description} | Deadline: {task.deadline}")



        elif choice == "11":

            print("👋 Exiting... Bye!")

            break


        else:

            print("❗ Invalid choice. Try again!")


if __name__ == "__main__":
    main()

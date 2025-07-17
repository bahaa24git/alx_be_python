task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is of high priority. Please complete it as soon as possible.")

    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed within the week.")
        else:
             print(f"Note: '{task}' is of medium priority. You can complete it within the week.")

    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be completed at your convenience.")
        else:
           print(f"Note: '{task}' is of low priority. You can complete it when you have time.")

    case _:
        print("Invalid priority level.")
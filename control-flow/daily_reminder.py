task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ")
time_bound = input("Is this task time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Task '{task}' is of high priority. Please complete it as soon as possible.")

    case "medium":
        print(f"Task '{task}' is of medium priority. You can complete it within the week.")
    case "low":
        print(f"Task '{task}' is of low priority. You can complete it when you have time.")
    case _:
        print("Invalid priority level.")
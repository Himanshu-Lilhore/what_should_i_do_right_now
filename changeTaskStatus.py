from functions import *
import json
from addHours import showActiveTasks


def changeTaskStatus():
    print("[1] Activate a task")
    print("[2] Deactivate a task")
    choice = int(input("Choose an option : "))
    if choice == 1:
        activateTask()
    elif choice == 2:
        deactivateTask()


def activateTask():
    parsed = parseJson()
    inactiveTasks = parsed["inactiveTasks"]
    if len(inactiveTasks) == 0:
        print("No inactive tasks found")
        return
    for task in inactiveTasks:
        print(f'{task}. {parsed["tasks"][str(task)][0]}')
    choice = int(input("Choose a task to activate : "))
    if choice > parsed["totalTasks"] or choice < 1:
        print("Invalid selection")
        return
    if choice in inactiveTasks:
        inactiveTasks.remove(choice)
    else:
        print("That task is already active")
        return
    parsed["inactiveTasks"] = inactiveTasks
    writeToJson(parsed)
    print(f'Activated task {choice}. {parsed["tasks"][str(choice)][0]}')


def deactivateTask():
    parsed = parseJson()
    showActiveTasks(parsed)
    choice = int(input("Deactivate task no. : "))
    if choice > len(parsed["tasks"]) or choice < 1:
        print("Invalid task number")
    else:
        if choice not in parsed["inactiveTasks"]:
            parsed["inactiveTasks"].append(choice)
    writeToJson(parsed)
    print(f"Task {choice} deactivated successfully")

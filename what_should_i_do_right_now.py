import time
import datetime
from showOptions import showOptions
from functions import *
from addNewTask import addNewTask
from showDatabase import showDatabase
from addHours import addHours
from changeTaskStatus import changeTaskStatus
from showFullHistory import showFullHistory

while True:
    print("""\nYour options are ..
    [1] : What should I do right now ?
    [2] : Add a new task
    [3] : Add my hard work
    [4] : Show the whole database
    [5] : Activate / Deactivate a task
    [6] : Show full history (till 3 days back)
        """)
    choice = int(input("Choose one option from above : "))

    if choice == 1:
        showOptions()   # improve

    elif choice == 2:
        addNewTask()

    elif choice == 3:
        addHours()

    elif choice == 4:
        showDatabase()

    elif choice == 5:
        changeTaskStatus()

    elif choice == 6:
        showFullHistory()

    choice = int(input("\n[0] - Exit\n[1] - Go again : "))
    if choice == 0:
        break


'''
json file structure :
{
    "totalTasks" : int,
    "wipeTime" : int,
    "inactiveTasks": [stores index(str) of deactivated tasks],
    "tasks" : {
            "1": [
                "taskName",
                totalHrs,
                totalHrsLast3Days,
                [list for dateTime of hrs added in last 3 days [timestamp(float), hrs]]
            ],
            ...
        }
}
'''

import json
import time
import datetime
from functions import *


def addNewTask():
    parsed = parseJson()

    totalTasks = parsed["totalTasks"] + 1
    parsed["totalTasks"] = totalTasks

    task = str(input("What is the task? : "))
    parsed["tasks"][totalTasks] = [task, 0.0, 0.0, []]

    writeToJson(parsed)

    print("Added task successfully ... ")
    print(f"{totalTasks}. {task} -")
    print(f"   -- Total Hours       : 0.0")
    print(f"   -- Hours last 3 days : 0.0")
    print(f"   -- Timestamps        : []")

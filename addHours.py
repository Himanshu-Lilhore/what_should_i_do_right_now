import json
import time
import datetime
from functions import *


def showActiveTasks(parsed):
    print()
    for task in parsed["tasks"]:
        if isActive(task, parsed):
            print(f'{task}. {parsed["tasks"][task][0]}')


def addHours():
    parsed = parseJson()
    showActiveTasks(parsed)
    taskNum = str(input("Which task   : "))
    if int(taskNum) in parsed["inactiveTasks"]:
        print("Cannot add hrs to an inactive task")
        print("Failed to add hrs")
        return
    hrs = float(input("How many hrs : "))
    thisTask = parsed["tasks"][taskNum]
    thisTask[1] = thisTask[1] + hrs
    thisTask[3].append([time.time(), hrs])
    parsed["tasks"][taskNum] = thisTask
    writeToJson(parsed)
    print(f"Successfully added {hrs} hrs to '{thisTask[0]}'")

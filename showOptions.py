import json
import time
import datetime
from functions import *


def myFunc(value):
    return value[1]


def showOptions():
    evaluateNow()
    parsed = parseJson()
    totalInXdays = 0.0    # total hrs worked in last X (wipeTime) days here
    tasks = parsed["tasks"]
    hrsForEach = []       # list of lists for total hrs work done in X days for each task
    maxLenTaskName = 0
    for task in tasks:
        if isActive(task, parsed):
            hrsForEach.append([task, tasks[task][2]])
            totalInXdays = totalInXdays + tasks[task][2]
            length = len(tasks[task][0])
            if maxLenTaskName < length:
                maxLenTaskName = length
    hrsForEach.sort(key=myFunc)
    count = 1
    print("\nYOUR OPTIONS ARE ...")
    for each in hrsForEach:
        if count == 3:
            print("-" * (maxLenTaskName + 14))
        print(f"{count}. {tasks[each[0]][0]} : {each[1]} hrs")
        count = count + 1

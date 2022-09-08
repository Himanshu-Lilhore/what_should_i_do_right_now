from functions import *
import datetime
import json


def showFullHistory():
    evaluateNow()
    deletedTime = open("deletedTimestamps.txt", "r")
    lines = deletedTime.readlines()

    parsed = parseJson()
    tasks = parsed["tasks"]

    for line in lines:
        things = line.strip("]\n ").split(", ")
        hrs = things[1]
        things = things[0].split(" [")
        taskNum, timestamp = things
        datetimeObj = stampToDate(float(timestamp))
        value = f'{datetimeObj:%d/%m/%y (%H:%M)}'
        print(f'{value} : {tasks[taskNum][0]} : {hrs} hrs')
    deletedTime.close()

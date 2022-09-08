import json
import time
import datetime


def parseJson():
    file = open("Data.json", "r")
    parsed = json.load(file)
    return parsed


def writeToJson(parsed):
    jsonObj = json.dumps(parsed, indent=4)
    with open("Data.json", "w") as file:
        file.write(jsonObj)


def stampToDate(value):
    return datetime.datetime.fromtimestamp(value)


def dateToStamp(value):
    return value.datetime.timestamp()


def evaluateNow():
    parsed = parseJson()
    delTym = open("deletedTimestamps.txt", "a")
    wipeTime = parsed["wipeTime"]
    count = 0.0
    timeNow = datetime.datetime.now()
    buffer = datetime.timedelta(days=wipeTime)
    time3DaysBack = timeNow - buffer
    tasks = parsed["tasks"]
    for task in tasks:
        count = 0.0
        stampList = tasks[task][3]
        delThese = []
        for that in stampList:
            stamp = stampToDate(that[0])
            hrs = that[1]
            if time3DaysBack > stamp:
                delTym.write(str(task) + " " + str(that) + "\n")
                #print(f"{time3DaysBack} > {stamp} , So Removed {that}")
                delThese.append(that)
            else:
                #print(f"{time3DaysBack} < {stamp} , So KEPT {that}")
                count = count + hrs
        for that in delThese:
            stampList.remove(that)
        tasks[task][2] = count
        tasks[task][3] = stampList
    parsed["tasks"] = tasks
    delTym.close()
    writeToJson(parsed)


def printTaskDetails():
    parsed = parseJson()
    tasks = parsed["tasks"]
    status = ""
    for task in tasks:
        if int(task) in parsed["inactiveTasks"]:
            status = "[In-active]"
        else:
            status = ""
        print(f"{task}. {status}{tasks[task][0]} -")
        print(f"   -- Total           : {tasks[task][1]} hrs")
        print(f"   -- Last 3 days     : {tasks[task][2]} hrs")
        print(f"   -- Timestamps      :", end="")
        timeStamps = tasks[task][3]
        for each in timeStamps:
            datetimeObj = stampToDate(each[0])
            value = f'{datetimeObj:%d/%m/%y(%H:%M)}'
            print(f" [{value}, {each[1]} hrs]", end="")
        print()


def isActive(value, parsed):
    if int(value) in parsed["inactiveTasks"]:
        return False
    else:
        return True

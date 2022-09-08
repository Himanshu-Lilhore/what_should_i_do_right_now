import json
from functions import *


def resetValues():
    parsed = parseJson()

    tasks = parsed["tasks"]
    for task in tasks:
        name = tasks[task][0]
        empty = [name, 0.0, 0.0, []]
        tasks[task] = empty

    writeToJson(parsed)


resetValues()

import json
import time
import datetime
from functions import *


def showDatabase():
    evaluateNow()
    parsed = parseJson()
    writeToJson(parsed)
    printTaskDetails()

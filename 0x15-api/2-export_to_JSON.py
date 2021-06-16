#!/usr/bin/python3
"""File for API"""

import json
import requests
import sys


def export_to_json(employeeID):
    """Exporting info gathered to Json file"""
    username = ''
    userDict = {}

    print("userDict: {}".format(userDict))

    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(employeeID))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos/'
                         .format(employeeID))

    username = users.json().get('username')
    todosJson = todos.json()

    userDict[employeeID] = []

    for task in todosJson:
        taskDict = {}
        taskDict["task"] = task.get('username')
        taskDict["username"] = username
        taskDict["completed"] = task.get('completed')

        userDict[employeeID].append(taskDict)

    with open("{}.json".format(employeeID), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

    return 0

if __name__ == "__main__":
    export_to_json(sys.argv[1])

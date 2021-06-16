#!/usr/bin/python3
"""File for API"""

import json
import requests


def export_allto_json():
    """Exporting all info gathered to Json file"""
    user_and_tasks = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    userInfo = {}
    for user in users:
        userInfo[user['id']] = user['username']

    for task in todos:
        if user_and_tasks.get(task['userId'], False) is False:
            user_and_tasks[task['userId']] = []

        taskDict = {}
        taskDict["username"] = userInfo[task['userId']]
        taskDict["task"] = task['title']
        taskDict["completed"] = task['completed']

        user_and_tasks[task['userId']].append(taskDict)

    with open("todo_all_employees.json", 'w') as jsonFile:
        json.dump(user_and_tasks, jsonFile)

    return 0

if __name__ == "__main__":
    export_allto_json()

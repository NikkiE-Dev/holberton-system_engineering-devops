#!/usr/bin/python3
"""File for API"""

import requests
import sys


def employ_task(employeeID):
    """Gathing employee info"""
    name = ''
    task_list = []
    compl_task = 0

    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(employeeID))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos/'
                         .format(employeeID))

    # Get the JSON from responses
    name = users.json().get('name')
    todosJson = todos.json()

    # loop the task
    for task in todosJson:
        if task.get('completed') is True:
            compl_task += 1
            task_list.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, compl_task, len(todosJson)))

    # Loop the task_list and print tasks
    for title in task_list:
        print("\t {}".format(title))

    return 0

if __name__ == "__main__":
    employ_task(sys.argv[1])

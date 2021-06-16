#!/usr/bin/python3
"""This is for API"""
import csv
import requests
import sys


def save_to_csv(employeeID):
"""Saving info gathered to CSV file"""
    username = ''
    allTasks = []

    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employeeID))
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos/'.format(employeeID))

    username = users.json().get('username')
    todosJson = todos.json()

    for task in todosJson:
        taskRow = []
        taskRow.append(employeeID)
        taskRow.append(username)
        taskRow.append(task.get("completed"))
        taskRow.append(task.get("title"))

        allTasks.append(taskRow)

    with open("{}.csv".format(employeeID), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(allTasks)
    return 0

if __name__ == "__main__":
    save_to_csv(sys.argv[1])

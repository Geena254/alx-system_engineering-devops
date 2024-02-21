#!/usr/bin/python3
"""
Accessing a REST API and returning information about todo lists of employees
"""


import requests
import sys


if __name__ == '__main__':
    employeeID = sys.argv[1]
    baseURL = "https://jsonplaceholder.typicode.com/users"
    url = baseURL + "/" + employeeID

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    tasks_done = []

    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in tasks_done:
        print("\t {}".format(task.get('title')))

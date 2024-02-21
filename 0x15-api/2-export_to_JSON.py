#!/usr/bin/python3
"""Accessing a REST API and returning information about todo lists of employees,
   then exporting the data in JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeID = sys.argv[1]
    baseURL = "https://jsonplaceholder.typicode.com/users"
    url = baseURL + "/" + employeeID

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # Create JSON file
    dictionary = {employeeID: []}
    for task in tasks:
        dictionary[employeeID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })
        with open('{}.json'.format(employeeID), 'w') as file_name:
            json.dump(dictionary, file_name)

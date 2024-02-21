#!/usr/bin/python3
"""
Accessing a REST API and returning information about todo lists of
employees, then exporting the data in CSV format.
"""


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

    with open('{}.csv'.format{employeeID), 'w') as file:  # Create CSV file
        for task in tasks:  # Export task data to CSV
            file.write('"{}","{}","{}","{}"\n'.format(employeeId, username,
                                                      task.get('completed'),
                                                      task.get('title')))

#!/usr/bin/python3
"""Accessing a REST API and returning information about todo lists of employees,
   then exporting the data in CSV format.
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

    # Create CSV file
    csv_file = f"{employeeID}.csv"
    with open(csv_file, mode='w', newline='') as file:
        # Export task data to CSV
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                    .format(employeeID, username, task.get('completed'),
                        task.get('title')))

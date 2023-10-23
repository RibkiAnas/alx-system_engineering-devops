#!/usr/bin/python3
"""
script that, using this REST API :
https://jsonplaceholder.typicode.com/, for
a given employee ID, returns information
about his/her TODO list progress and export
data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    # Get the employee data from api
    employee_id = sys.argv[1]
    employee_url = base_url + "users/" + employee_id
    employee_data = requests.get(employee_url).json()

    # Get the employee username
    employee_username = employee_data["username"]

    # Get the employee TODO list
    todo_url = base_url + "todos?userId=" + employee_id
    todo_data = requests.get(todo_url).json()

    # Open a csv file with the employee id as the name
    with open(f"{employee_id}.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            task_completed = task["completed"]
            task_title = task["title"]
            csv_writer.writerow([employee_id, employee_username,
                                 task_completed, task_title])

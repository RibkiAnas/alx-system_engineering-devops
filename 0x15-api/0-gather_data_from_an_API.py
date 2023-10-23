#!/usr/bin/python3
"""
script that, using this REST API :
https://jsonplaceholder.typicode.com/, for
a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    # Get the employee data from api
    employee_id = sys.argv[1]
    employee_url = base_url + "users/" + employee_id
    employee_data = requests.get(employee_url).json()

    # Get the employee name
    employee_name = employee_data["name"]

    # Get the employee TODO list
    todo_url = base_url + "todos?userId=" + employee_id
    todo_data = requests.get(todo_url).json()

    # Count the number of completed and total tasks
    completed_tasks = 0
    total_tasks = len(todo_data)

    completed_titles = []

    for task in todo_data:
        if task["completed"]:
            completed_tasks += 1
            completed_titles.append(task["title"])

    # Display TODO list progress on the stdout
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))
    for title in completed_titles:
        print(f"\t {title}")

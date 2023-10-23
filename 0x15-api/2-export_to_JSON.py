#!/usr/bin/python3
"""
script that, using this REST API :
https://jsonplaceholder.typicode.com/, for
a given employee ID, returns information
about his/her TODO list progress export
data in the JSON format.
"""
import json
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

    tasks_list = []

    for task in todo_data:
        task_title = task["title"]
        task_completed = task["completed"]

        task_dict = {
                "task": task_title,
                "completed": task_completed,
                "username": employee_username
                }

        tasks_list.append(task_dict)

        user_dict = {
                str(employee_id): tasks_list
                }

        with open(f"{employee_id}.json", "w") as json_file:
            json.dump(user_dict, json_file)

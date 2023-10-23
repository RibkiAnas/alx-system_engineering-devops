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
    # Get the list of all employees from api
    users_url = base_url + "users/"
    users_data = requests.get(users_url).json()

    all_users_dict = {}

    for user in users_data:
        user_id = str(user["id"])
        user_username = user["username"]

        todo_url = base_url + "todos?userId=" + user_id
        todo_data = requests.get(todo_url).json()

        tasks_list = []

        for task in todo_data:
            task_title = task["title"]
            task_completed = task["completed"]

            task_dict = {
                    "username": user_username,
                    "task": task_title,
                    "completed": task_completed
                    }

            tasks_list.append(task_dict)

        all_users_dict[str(user_id)] = tasks_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_users_dict, json_file)

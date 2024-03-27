#!/usr/bin/env python3
"""Accessing a REST API for todo lists of employees."""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    endpoint = f"{base_url}/{employee_id}"

    response = requests.get(endpoint)
    employee_name = response.json().get("name")

    todo_url = f"{endpoint}/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    total_done = 0
    done_tasks = []

    for task in tasks:
        if task.get("completed"):
            done_tasks.append(task)
            total_done += 1

    print(f"Employee {employee_name} is done with tasks "
          f"({total_done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t{task['title']}")
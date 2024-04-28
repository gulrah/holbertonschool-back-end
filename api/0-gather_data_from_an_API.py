#!/usr/bin/python3

"""Script"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = base_url + "/users/{}".format(employee_id)
    todo_url = base_url + "/todos?userId={}".format(employee_id)

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        done_tasks = [task for task in todo_data if task['completed']]
        total_tasks = len(todo_data)
        num_done_tasks = len(done_tasks)

        print("Employee {} is done with tasks({}/{}):".format(user_data['name'], num_done_tasks, total_tasks))
        for task in done_tasks:
            print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

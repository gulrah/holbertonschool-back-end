#!/usr/bin/python3
"""Script"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    
    all_tasks = {}
    
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        
        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        tasks = requests.get(url).json()
        
        user_tasks = []
        for task in tasks:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_dict)
            
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)

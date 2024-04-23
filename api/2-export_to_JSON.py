#!/usr/bin/python3
"""Script"""

import json
import requests
import sys

def fetch_and_export_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    
    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
        
        employee_id = user_data['id']
        employee_name = user_data['username']
        json_filename = f"{employee_id}.json"
        
        tasks = []
        for task in todos_data:
            tasks.append({"task": task['title'], "completed": task['completed'], "username": employee_name})
            
            with open(json_filename, mode='w') as json_file:
                json.dump({str(employee_id): tasks}, json_file, indent=4)
                
                print(f"Data exported to {json_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
        
if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
        
        employee_id = int(sys.argv[1])
        fetch_and_export_todo_list(employee_id)

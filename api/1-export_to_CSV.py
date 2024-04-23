#!/usr/bin/env python3
"""TODO"""

import csv
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
        employee_name = user_data['name']
        csv_filename = f"{employee_id}.csv"
        
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            
            for task in todos_data:
                csv_writer.writerow([employee_id, employee_name, task['completed'], task['title']])
                
        print(f"Data exported to {csv_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
        
if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
        
        employee_id = int(sys.argv[1])
        fetch_and_export_todo_list(employee_id)

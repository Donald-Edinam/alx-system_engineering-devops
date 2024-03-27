import requests

def get_employee_todo_progress(employee_id):
    # request from server
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    server_response = requests.get(url)
    if server_response.status_code != 200:
        print(f"Error: User {employee_id} not found")
        return None
    
    # Get the employee name
    employee_name = server_response.json()["name"]

    # Fetching the todo items for the user
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    completed_tasks = []
    total_tasks = 0

    for todo in todos_response.json():
        total_tasks += 1
        if todo["completed"]:
            completed_tasks.append(todo["title"])


    # Step 9: Display the results
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):\n")
    for task in completed_tasks:
        print(f"\t{task}\n")

if __name__ == "__main__":
    import sys

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
# Import the 'datetime' module, which will be handle dates
import datetime

# Defines a 'Task' class with an 'init' constructor that initializes the attributes of a task
class Task:
    def __init__(self, title, description, priority, due_date, category):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category 
        
# Defines a TaskManager class with a tasks list to store instances of the Task class
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    # Add a task
    def add_task(self, task):
        self.tasks.append(task)
        
    # Delete a task
    def delete_task(self, index):
        try:
            del self.tasks[index]
            print("Task deleted!")
            
        except IndexError:
            print("Task index invalid!")
            
    # Update a task
    def update_task(self, index, updated_task):
        try:
            self.tasks[index] = updated_task
            print("Task updated!")
            
        except IndexError:
            print("Task index invalid!")

    # List tasks
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return
        
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.title} - Description: {task.description} - Priority: {task.priority} - Due Date: {task.due_date}")
            
# Defines a 'get_user_input' function to get user input, removing extra spaces.
def get_user_input(prompt):
    return input(prompt).strip()


            
    

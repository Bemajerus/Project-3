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
        

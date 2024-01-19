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

# Defines a get_priority function to get the task priority from the user, ensuring it is a valid option (High, Medium, or Low).
def get_priority():
    while True:
        priority = get_user_input("Enter task priority (High/Medium/Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            return priority
        
        else:
            print("Invalid priority. Please enter High, Medium or Low")
            
# Defines a get_due_date function to get the task's due date from the user, ensuring it is in the correct format (YYYY-MM-DD).
def get_due_date():
    while True:
        date_str = get_user_input("Enter due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return due_date
        
        except ValueError:
            print("Date format invalid, please use YYYY-MM-DD")
            
# Defines the main main function. In the while loop, displays the menu, gets the user's choice, and performs the corresponding action.
def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu:")
        print("1 - Add Task")
        print("2 - List Tasks")
        print("3 - Delete Task")
        print("4 - Update Task")
        print("5 - Exit")
        
        choice = get_user_input("Enter your choice (1-5): ")
        
        # If the user's choice is "1", prompts for information about the new task, creates an instance of Task, adds it to the task list, and informs the user that the task was added successfully.
        if choice == "1":
            title = get_user_input("Enter task title: ")
            description = get_user_input("Enter task description: ")
            priority = get_priority()
            due_date = get_due_date()
            category = get_user_input("Enter task category: ")
            
            new_task = Task(title, description, priority, due_date, category)
            task_manager.add_task(new_task)
            print("Task added!")
            
        # If the user's choice is "2", displays the list of tasks using the list_tasks method of the TaskManager class.
        elif choice == "2":
            print("\nTask List:")
            task_manager.list_tasks()
            
        # If the user's choice is "3", prompts for the task index to delete, converts it to an integer, and calls the delete_task method of the TaskManager class.
        elif choice =="3":
            index = int(get_user_input("Enter the task index to delete: ")) -1
            task_manager.delete_task(index)
            
        # If the user's choice is "4", prompts for the task index to update and new task information, converts the index to an integer, creates an instance of Task, and calls the update_task method of the TaskManager class.
        elif choice == "4":
            index = int(get_user_input("Enter the task index to update: ")) -1
            title = get_user_input("Enter updated task title: ")
            description = get_user_input("Enter updated task description: ")
            priority = get_priority()
            due_date = get_due_date()
            category = get_user_input("Enter updated task category: ")
            
            updated_task = Task(title, description, priority, due_date, category)
            task_manager.update_task(index, updated_task)
            
        # If the user's choice is "5", prints an exit message and breaks the loop, ending the program.
        elif choice == "5":
            print("Exiting Task Manager!")
            
            break
        
        # If the user's choice is not one of the valid options, informs that the choice is invalid.
        else:
            print("Invalid choice, please enter a number between 1 and 5")
            
# Calls the main function when the script is executed as a main program. This ensures that the code inside main() is executed only when the script is run, not when it is imported as a module.
if __name__ == "__main__":
    main()
            
        
        
        

            
    

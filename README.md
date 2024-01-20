# Task Manager

Task Manager simplifies task management with an easy-to-use interface and robust functionality. Developed using Python, this console application allows users to efficiently add, list, update, and delete tasks, providing a streamlined solution for organizing activities.

## Features

Built upon the fundamentals of Python programming, the Task Manager employs standard programming constructs to offer a comprehensive set of features. Users can interact with the application through the console, performing actions such as adding tasks, listing existing tasks, updating task details, and deleting tasks.

### Existing Features

- __Task Management Functions__

  - Users can add new tasks, providing details such as title, description, priority, due date, and category.
  - The application supports listing tasks, displaying essential information like title, priority, and due date.
  - Tasks can be deleted, offering users the flexibility to remove completed or unnecessary items.
  - An update feature allows users to modify task details, ensuring the information remains accurate and relevant.

- __Console Interface__

  - The user interacts with the Task Manager through a console-based menu system, making it straightforward and accessible.
  - A menu displays options for adding tasks, listing tasks, updating tasks, and deleting tasks, providing a clear navigation structure.
  - User input is gathered through simple prompts, ensuring a user-friendly experience.

### Code Structure

- __Task Class__
  - Defines a Task class with attributes such as title, description, priority, due_date, and category.
 
- __TaskManager Class__
  - Implements a TaskManager class with methods to add, list, update, and delete tasks.
 
- __User Input Functions__
  - Includes functions like get_user_input, get_priority, and get_due_date to gather user input and validate data.

- __Main Functionality__
  - The main function initializes a TaskManager instance and runs a loop to present a menu for user interaction.
  - Depending on the user's choice, the application performs the corresponding task management operation.

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
  - Invalid user inputs are handled gracefully, providing appropriate feedback and allowing users to correct their input.

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

## Testing

The application has undergone testing to ensure robust functionality and a positive user experience.

- __Functionality Tests__
  - Each task management function has been tested to guarantee accurate task addition, listing, updating, and deletion.

- __Code Validators__
  - The Python code has been validated using PEP8 to maintain consistent style and readability.
  - No errors were found when passing through the official PEP8 validator.

### Validator Testing

- __Python(PEP8)__
  -  No errors were returned when passing through the official PEP8 validator.

## Future Enhancements

The Task Manager project can be expanded by incorporating additional features such as task prioritization, due date reminders, and user authentication. Regular updates and improvements will contribute to a more robust and versatile task management tool.

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- __Steps for deployment__
  - Fork or clone this repository.
  - Create a new Hekoku app.
  - Set the buildbacks to Python and NodeJS in that order.
  - Link the Heroku app to the repository.
  - Click on Deploy.

### How to Clone

1. Log into your account on github
2. Go to the repository of this project Bemajerus/Project-3/
3. Click on the code button, and copy your preferred clone link.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal, paste the link you copied in step 3 and press enter.

### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, Bemajerus/Project-3/
3. Click the Fork button in the top right corner.

## Credits

- Code Institute for the deployment terminal.

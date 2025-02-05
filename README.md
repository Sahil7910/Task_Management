# Task Management Application

## Overview
The Task Management Application is a simple command-line tool designed for efficient task tracking and management. It supports basic CRUD operations and ensures tasks are stored persistently for later use.

---

## Features
- **Add a Task**: Add tasks with a description, deadline, and status.
- **View Tasks**:
  - View all tasks.
  - Filter tasks by status: pending or completed.
- **View Pending Tasks**:Filter and display only pending tasks.
-	**View Completed Tasks**:Filter and display only completed tasks.
-	**Sort Tasks**:sorting tasks by deadline or status. 
- **Update a Task Description**: Update the description.
- **Update a Task status**: Umark a task as completed.
- **Search Task**:user can search for tasks containing a specific word
- **Due Date Reminders**:Notify users about tasks that are due soon
- **Delete a Task**: Remove tasks from the list.
- **Persistent Storage**:
  - Store tasks in an SQLite database.

---
# Assumptions and Design Decisions

## Task Properties:
- **Title**: Each task must include a title.
- **Description**: A brief description is required for each task.
- **Status**: Each task has a status, which can either be *Pending* or *Completed*.
- **Deadlines**: Deadlines are optional and can be left blank if not applicable.
- **Unique Identifier**: Each task is identified uniquely by an internal ID, which is automatically generated by the system.

## Database Design:
- **SQLite**: SQLite is chosen as the database due to its simplicity and seamless integration with lightweight applications.
- **Single Table**: The database contains a single table called `tasks` to store all task-related details.
- **Data Persistence**: All task data is persisted in the database, allowing for task management across application restarts.

## User Interface:
- **CLI-Based**: The application uses a command-line interface (CLI) for task management.
- **Input Validation**: Input validation is minimal, assuming the user will provide valid data (e.g., correct date formats for deadlines).

## Environment:
- The application is designed to run on any system with **Python 3.7+** installed.
- It assumes the presence of a **working terminal/command prompt** for execution.

## Dependencies:
- **Built-In Libraries**: Only built-in Python libraries are used to minimize external dependencies.

## Error Handling:
- Basic error handling is implemented for common scenarios:
  - Invalid input formats (e.g., entering text when a number is expected).
  - Missing tasks during updates or deletions.
  - Edge cases like simultaneous access in multi-user environments are **not** covered.

## Scalability:
- The application is designed for **single-user** usage and basic task management.
- It is **not designed** to handle high-concurrency environments or a distributed architecture.

## Design Choices:
- The codebase is structured into **modular functions** to enhance readability and maintainability.
- The project is structured to easily allow future migration to a GUI-based or web-based framework (e.g., **Flask** or **Django**).

## Assumptions:
- Users are assumed to be familiar with running Python scripts via the command line.
- It is assumed that users provide valid inputs for task creation and management.
- The application is intended to run in a **local development environment**.

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Sahil7910/Task_Management.git
2. Navigate to the project directory:
   ```bash
   cd Task_Management
4. Run the application:
   ```bash
   python main.py



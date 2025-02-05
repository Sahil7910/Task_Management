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



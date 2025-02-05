import sqlite3
from datetime import datetime, timedelta

# Database Connection
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        deadline TEXT,
        status TEXT DEFAULT 'Pending',
        priority TEXT DEFAULT 'Medium'
    )
""")
conn.commit()


# Task Model Class
class Task:
    def __init__(self, id=None, description="", deadline=None, status="Pending", priority="Medium"):
        self.id = id
        self.description = description
        self.deadline = deadline
        self.status = status
        self.priority = priority

    def __repr__(self):
        return f"Task(id={self.id}, description='{self.description}', deadline='{self.deadline}', status='{self.status}', priority='{self.priority}')"


# Function to add a new task
def add_task(description, deadline=None, priority="Medium"):
    cursor.execute("INSERT INTO tasks (description, deadline, priority) VALUES (?, ?, ?)", (description, deadline, priority))
    conn.commit()
    print("Task added successfully!\n")



def get_all_tasks(sort_by=None):
    if sort_by == "deadline":
        cursor.execute("SELECT * FROM tasks ORDER BY deadline ASC")
    elif sort_by == "status":
        cursor.execute("SELECT * FROM tasks ORDER BY status ASC")
    else:
        cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()
    return [Task(id=t[0], description=t[1], deadline=t[2], status=t[3], priority=t[4]) for t in tasks]



# Function to get tasks by status (Pending or Completed)
def get_tasks_by_status(status):
    cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
    tasks = cursor.fetchall()
    return [Task(id=t[0], description=t[1], deadline=t[2], status=t[3], priority=t[4]) for t in tasks]


# Function to update task status
def update_task_status(task_id, new_status):
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    print(" Task status updated!\n")

# Function to update task description
def update_task_description(task_id, new_description):
    cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id))
    conn.commit()
    print(" Task description updated!\n")

# Function to delete a task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print(" Task deleted successfully!\n")

def update_task_priority(task_id, new_priority):
    cursor.execute("UPDATE tasks SET priority = ? WHERE id = ?", (new_priority, task_id))
    conn.commit()
    print(" Task priority updated!\n")


def get_due_soon_tasks():
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    cursor.execute("SELECT * FROM tasks WHERE deadline <= ? AND status = 'Pending'", (tomorrow,))
    tasks = cursor.fetchall()
    return [Task(id=t[0], description=t[1], deadline=t[2], status=t[3], priority=t[4]) for t in tasks]

def search_tasks(keyword):
    cursor.execute("SELECT * FROM tasks WHERE description LIKE ?",('%' + keyword + '%',))
    tasks = cursor.fetchall()
    return [Task(id=t[0], description=t[1], deadline=t[2], status=t[3]) for t in tasks]


# Closing the database connection when done
def close_connection():
    conn.close()

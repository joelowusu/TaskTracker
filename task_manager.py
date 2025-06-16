from task import Task
import storage

# This class manages the list of tasks
class TaskManager:
    
    # Sets up the class with a file path and loads existing tasks
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = self.load_tasks()

    # Loads the tasks from the file
    def load_tasks(self):
        raw_tasks = storage.load_tasks(self.filepath)
        return [Task.from_dict(task) for task in raw_tasks]

    # Saves the tasks to the file
    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        storage.save_tasks(self.filepath, data)

    # Adds a new task to the list
    def add_task(self, title, description):
        self.tasks.append(Task(title, description))
        self.save_tasks()

    # Returns all tasks
    def list_tasks(self):
        return self.tasks

    # Deletes a task from the list using its index
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

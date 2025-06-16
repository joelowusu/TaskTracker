# This class is used to store task data
class Task:
    
    # Constructor for the Task class
    def __init__(self, title, description, status="pending"):
        # Stores the title of the task
        self.title = title
        # Stores the description of the task
        self.description = description
        # Stores the status of the task
        self.status = status

    # Converts the task into a dictionary
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    # Converts a dictionary back into a Task object
    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["description"], data["status"])


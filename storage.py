import json

# Loads task data from the JSON file
def load_tasks(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    # If the file doesn't exist it returns an empty list
    except FileNotFoundError:
        return []

# Saves task data to the JSON file
def save_tasks(filepath, tasks):
    with open(filepath, "w") as f:
        json.dump(tasks, f, indent=4)

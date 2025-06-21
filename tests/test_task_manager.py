import unittest
from task_manager import TaskManager
import os

# This test checks the TaskManager class
class TestTaskManager(unittest.TestCase):

    # Setup - creates a test file
    def setUp(self):
        self.test_file = "test_tasks.json"
        self.manager = TaskManager(self.test_file)

    # Clean up - deletes the test file after each test
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # Test if a task is added correctly
    def test_add_task(self):
        self.manager.add_task("Test", "Testing add")
        self.assertEqual(len(self.manager.list_tasks()), 1)

    # Test if a task is deleted correctly
    def test_delete_task(self):
        self.manager.add_task("Temp", "Delete me")
        self.manager.delete_task(0)
        self.assertEqual(len(self.manager.list_tasks()), 0)

    # Test if a task can be marked as complete
    def test_mark_complete(self):
        self.manager.add_task("Complete me", "Testing complete")
        self.manager.mark_complete(0)
        task = self.manager.list_tasks()[0]
        self.assertEqual(task.status, "complete")

# Run all tests
if __name__ == "__main__":
    unittest.main()

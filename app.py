from flask import Flask, render_template, request, redirect, url_for
from task_manager import TaskManager

# Tell Flask to use the 'pages' folder for HTML templates
app = Flask(__name__, template_folder="pages")
manager = TaskManager("tasks.json")

# Home page - shows all tasks
@app.route("/")
def index():
    tasks = manager.list_tasks()
    return render_template("index.html", tasks=tasks)

# Add new task
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        manager.add_task(title, description)
        return redirect(url_for("index"))
    return render_template("add.html")

# Delete task
@app.route("/delete/<int:index>")
def delete(index):
    manager.delete_task(index)
    return redirect(url_for("index"))

# Mark task as complete
@app.route("/complete/<int:index>")
def complete(index):
    manager.mark_complete(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, stream_template, render_template
from dataclasses import dataclass, field
from datetime import datetime

app = Flask(__name__)


@dataclass
class ToDoItems:
    text: str
    id: str = field(default_factory=lambda: datetime.now().isoformat())
    done: bool = field(default=False)

    def check(self, state):
        return ToDoItems(text=self.text, id=self.id, done=state)


todos = []


@app.route("/", methods=["GET"])
def main():
    return stream_template("index.html")


@app.route("/todos", methods=["POST"])
def create_todo():
    item = ToDoItems(text=request.form.get("toadd"))
    todos.append(item)
    return render_template("list_items.html", todos=todos)


@app.route("/todos-done/<id>", methods=["PUT"])
def mark_todo(id):
    global todos
    isdone = not request.form.get("done") == "False"
    todos = [item if item.id != id else item.check(not isdone) for item in todos]
    return render_template("list_items.html", todos=todos)


if __name__ == "__main__":
    print("run with `flask run --reload` or somth")

from flask import Flask, request, stream_template, render_template

app = Flask(__name__)

todos = []


@app.route("/", methods=["GET"])
def main():
    return stream_template("index.html")


@app.route("/todos", methods=["POST"])
def create_todo():
    print(request.form)
    todos.append(request.form.get("toadd"))
    return render_template("list_items.html", todos=todos)


if __name__ == "__main__":
    app.run()

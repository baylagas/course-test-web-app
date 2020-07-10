from flask import Flask, render_template, request, redirect
from database import Database

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/course", methods=["GET", "POST"])
def course():
    database = Database()
    if request.method == "GET":
        # codigo que toma el id y lo imprime
        # form a la tabla y ponganle el method="GET"
        # ocupar un input type=hidden para el id
        data = database.getAllCourse()
        print(data)
        return render_template("course.html", courses=data)
    else:
        print(request.form)
        name = request.form["name"]
        entity_name = request.form["entity_name"]
        rows = database.insertCourse(name, entity_name)
        print(f"{rows} rows affected")
        return redirect("/course")


if __name__ == "__main__":
    app.run(debug=True)

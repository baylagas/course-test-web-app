from flask import Flask, render_template, request, redirect
from database import Database
from urllib.parse import urlparse

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/course", methods=["GET", "POST"])
def course():
    database = Database()
    if request.method == "GET":
        print(urlparse)
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


@app.route("/course/update/<int:id>", methods=["GET", "POST"])
def update(id):
    # codigo que hara el update recibiendo el id
    database = Database()
    if request.method == "GET":
        data = database.getCourseById(id)
        return render_template("updateCourse.html", data=data, id=id)
    else:
        id = request.form["id"]
        name = request.form["name"]
        entity = request.form["entity_name"]
        rows = database.updateCourse(id, name, entity)
        print(f"{rows} rows affected")
        return redirect("/course")


@app.route("/course/delete/<int:id>", methods=["GET"])
def delete(id):
    database = Database()
    if request.method == "GET":
        rows = database.deleteCourseById(id)
        print(f"{rows} rows affected")
        return redirect("/course")


if __name__ == "__main__":
    app.run(debug=True)

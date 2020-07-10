from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/course", methods=["GET", "POST"])
def course():
    if request.method == "GET":
        print("get...")
        return render_template("course.html")
    else:
        print("post...")


if __name__ == "__main__":
    app.run(debug=True)

""" Simple flask application """

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from search.main import searching


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
# Init database
db = SQLAlchemy(app)


def create_db():
    with app.app_context():
        db.create_all()
        print("Database created")


@app.route("/")
def index():
    title = "Search"
    return render_template("index.html", title=title)


@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title=title)


@app.route("/results", methods=["POST"])
def results():
    unformatted_number = request.form.get("unformatted_number")
    if not unformatted_number:
        error_statement = "Phone number is requiared"
        return render_template("error.html", error_statement=error_statement)
    results = searching(unformatted_number)
    if results is not list():
        return render_template("error.html", error_statement=results)
    title = "Results"
    return render_template("results.html", title=title, results=results)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

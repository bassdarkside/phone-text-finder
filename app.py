""" Simple flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return "About page"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

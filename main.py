""" Simple flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    Функция index возвращает обработанный шаблон index.html.
    :return: результат вызова функции render_template("index.html").
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Функция «о» предоставляет информацию о функции.
    """
    return "About page"


if __name__ == "__main__":
    app.run(debug=True)

# coding: utf-8
# author: zpta
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello_person(name):
    return f"Hello, {escape(name)}"


if __name__ == '__main__':
    app.run(load_dotenv=True)

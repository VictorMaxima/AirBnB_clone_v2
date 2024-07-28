#!/usr/bin/python3
""" module for a script that sets up a simple flask application """
import flask
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ view function for the home page """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

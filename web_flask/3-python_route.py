#!/usr/bin/python3
""" module for a script that sets up a simple flask application """
import flask
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """ view function for the home page """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def view_hbnh():
    """ view function for hbnb """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def view_c(text):
    """ contains the c function """
    new_text = ""
    for i in text:
        if i == "_":
            new_text += " "
        else:
            new_text += i
    return "C " + new_text

@app.route("/python/<text>", strict_slashes=False)
def view_python(text):
    """ contains the dynamic python view function """
    new_text = ""
    for i in text:
        if i == "_":
            new_text += " "
        else:
            new_text += i
    return "Python " + new_text

@app.route("/python", strict_slashes=False)
def view_default_python():
    """ contains the python view function """
    return "Python is cool"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
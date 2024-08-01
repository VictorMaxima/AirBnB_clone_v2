#!/usr/bin/python3
""" module for a script that sets up a simple flask application """
import flask
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ view function for the home page """
    return "Hello HBNB!"


@app.teardown_appcontext
def clean(self):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    print_list = []
    for k, v in storage.all("State").items():
        print_list.append(v.to_dict())
    print_list.sort(key=lambda x: x['name'])
    return render_template("7-states_list.html", states=print_list)


@app.route("/cities_by_states", strict_slashes=False)
def list_cities_by_states():
    print_list = []
    for k, v in storage.all("State").items():
        result_dict = v.to_dict()
        id = result_dict.get("id")
        cities = storage.all("City")
        city_dict_list = []
        for k, v in cities.items():
            if v.to_dict().get("state_id") == result_dict.get("id"):
                city_dict_list.append(v.to_dict())
                city_dict_list.sort(key=lambda x: x['name'])
        result_dict['cities'] = city_dict_list
        print_list.append(result_dict)
    print_list.sort(key=lambda x: x['name'])
    return render_template("8-cities_by_states.html", states=print_list)


@app.route("/states", strict_slashes=False)
def states():
    return list_states()


@app.route("/states/<id>", strict_slashes=False)
def list_state_dynamic(id):
    result_dict = {}
    for k, v in storage.all("State").items():
        if v.to_dict().get("id") == id:
            result_dict['name'] = v.to_dict().get("name")
            break
    cities = storage.all("City")
    city_dict_list = []
    for k, v in cities.items():
        print(v.to_dict()['state_id'])
        if v.to_dict()['state_id'] == id:
            print(v.to_dict())
            city_dict_list.append(v.to_dict())
    city_dict_list.sort(key=lambda x: x['name'])
    result_dict['cities'] = city_dict_list
    return render_template("9-states.html", state=result_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

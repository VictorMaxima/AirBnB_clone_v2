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
    return render_template("7-states_list.html", states = print_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
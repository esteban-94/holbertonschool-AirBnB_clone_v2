#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """s"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)

@app.route('/states/<text>', strict_slashes=False)
def python(text):
    """s"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=text)

@app.teardown_appcontext
def teardown_db(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

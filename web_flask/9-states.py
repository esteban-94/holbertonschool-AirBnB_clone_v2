#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def get_state_by_id(id):
    """Display a HTML page of a State and their cities"""
    states = storage.all(State).values()

    for state in states:
        if id == state.id:
            return render_template('9-states.html',
                                    state=state, cities=state.cities)

    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

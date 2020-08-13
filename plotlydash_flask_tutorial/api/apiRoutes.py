"""Routes for parent Flask app."""
from flask import render_template, jsonify
from flask import current_app as app

# import jsonify

from .users import getUsersFunction, postUsersFunction


@app.route('/api')
def api():
    """Landing page."""
    return render_template(
        'index.jinja2',
        title='Plotly Dash Flask Tutorial',
        description='Embed Plotly Dash into your Flask applications.',
        template='home-template',
        body="This is a homepage served with Flask."
    )

@app.route('/api/tasks')
def getTasks():
    """JSON"""

    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web', 
            'done': False
        }
    ]

    return {'tasks': tasks}

@app.route('/api/users')
def getUsers():
    """Subbed this to another file"""
    users = getUsersFunction()
    return {'users': users}

@app.route('/api/users/<string:name>', methods=['POST'])
def postUsers(name):
    """Subbed this to another file"""
    newUser = postUsersFunction(name)
    # return { 'message': f'{name} added', 'newUser': newUser }
    return jsonify(message=f'{name} added', newUser=newUser )

# @app.route('/users/<string:name>', methods=['POST'])
# def addUserByName(name):
#     usersList.append(name)
#     return jsonify({ 'message': 'New user added'  })
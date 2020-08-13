"""Routes for parent Flask app."""
from flask import render_template, jsonify
from flask import current_app as app

from .users import getUsersFunction, postUsersFunction


@app.route('/api')
def api():
    return jsonify({
      'routeList': [
        {
          'route': '/api',
          'method': 'GET',
          'description': 'Get API help'
        },
        {
          'route': '/api/tasks',
          'method': 'GET',
          'description': 'Get task list'
        },
        {
          'route': '/api/users',
          'method': 'GET',
          'description': 'Get user list'
        },
        {
          'route': '/api/users/<string:name>',
          'method': 'POST',
          'description': 'Add a user'
        },
      ]
    })

    # 'routeTree1': {
    #     'api': {
    #       'route': '/api',
    #       'methods': 'GET',
    #       'childRoutes': {
    #         'tasks': {
    #           'route': '/api/tasks',
    #           'methods': 'GET'
    #         },
    #         'users': {
    #           'route': '/api/users',
    #           'methods': 'GET'
    #         },
    #         'users/<string:name>': {
    #           'route': '/api/users/<string:name>',
    #           'methods': 'POST'
    #         },
    #       }
    #     }
    #   },
    #   'routeTree2': {
    #     'GET: api': [
    #       'GET: tasks',
    #       'GET: users',
    #       'POST: users/<string:name>'
    #     ]
    #   },

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

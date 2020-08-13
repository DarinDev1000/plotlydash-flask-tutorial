
users = [
        {
            'id': 1,
            'name': u'Darin'
        },
        {
            'id': 2,
            'name': u'David'
        }
    ]

def getUsersFunction():
    return {'users': users}

def postUsersFunction(name):
    newUser = {
                'id': len(users)+1,
                'name': name
            }
    users.append(newUser)
    return {'newUser': newUser}

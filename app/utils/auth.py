from flask import session, redirect
from functools import wraps

# functools contains helper functions that change other functions
# wraps() is a decorator

def login_required(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        #print('wrapper')
        if session.get('loggedIn') == True:
            return func(*args, **kwargs)

        return redirect('/login')

    return wrapped_function
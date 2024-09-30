from flask import redirect, url_for
from flask_login import current_user
from functools import wraps

def login_forbidden(f):
    @wraps(f)
    def dec(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('game.home'))
        return f(*args, **kwargs)

    return dec
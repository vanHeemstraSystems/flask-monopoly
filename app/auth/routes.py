from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user
from app import db, bcrypt
from app.auth.forms import RegistrationForm
from app.auth.models import User

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pwd_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=pwd_hash, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('sign_up.html', form=form)

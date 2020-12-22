import os
from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app_settings = 'app.config.Config'

    app.config.from_object(app_settings)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    assets = Environment(app)
    assets.url = app.static_url_path
    scss = Bundle('scss/style.scss', 'scss/tiles.scss', filters='pyscss', output='css/all.css')
    assets.register('scss_all', scss)
    js = Bundle('js/updateDisplay.js', output='js/build.js')
    assets.register('js_build', js)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    from app.auth.routes import auth
    from app.game.routes import game

    app.register_blueprint(game, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app

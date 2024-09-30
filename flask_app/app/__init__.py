#!/usr/bin/env python
import sass
from flask import Flask
from flask_assets import Environment, Bundle
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app_settings = 'app.config.Config'
    app.config.from_object(app_settings)
    assets = Environment(app)
    assets.url = app.static_url_path
    # create bundle for Flask-Assets to compile and prefix scss to css
    test = Bundle('scss/test.scss', filters='libsass', output='css/test.css')
    assets.register('test', test)
    test.build() - Superfluous
    scss = Bundle('scss/style.scss', 'scss/tiles.scss', filters='libsass', output='css/all.css')
    assets.register('scss_all', scss)
    scss.build()
    # general = Bundle('scss/variables.scss', 'scss/navbar.scss',  filters='libsass', output='css/general.css')
    # assets.register('general', general)
    # general.build() - Superfluous
    # custom_scss = Bundle('scss/customs.scss', filters='pyscss', output='css/customs.css')
    # assets.register('customs', custom_scss)
    # custom_scss.build()

    # home_scss = Bundle('scss/pages/home.scss', filters='pyscss', output='css/pages/home.css')
    # assets.register('home_scss', home_scss)
    # home_scss.build() - Superfluous
    # menu_scss = Bundle('scss/pages/menu.scss', filters='pyscss', output='css/pages/menu.css')
    # assets.register('menu_scss', menu_scss)
    # menu_scss.build() - Superfluous
    # join_scss = Bundle('scss/pages/join_game.scss', filters='pyscss', output='css/pages/join_game.css')
    # assets.register('join_scss', join_scss)
    # join_scss.build() - Superfluous
    # waiting_room_scss = Bundle('scss/pages/waiting_room.scss', filters='pyscss', output='css/pages/waiting_room.css')
    # assets.register('waiting_room_scss', waiting_room_scss)
    # waiting_room_scss.build() - Superfluous
    # profile_scss = Bundle('scss/pages/profile.scss', filters='pyscss', output='css/pages/profile.css')
    # assets.register('profile_scss', profile_scss)    
    # profile_scss.build() - Superfluous

    js = Bundle('js/throttle.js', 'js/selectors.js', 'js/buildOnField.js', 'js/updateDisplay.js', output='js/build.js')
    assets.register('js_build', js)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    socketio.init_app(app)
    socketio.cors_allowed_origins = "*"

    from app.auth.routes import auth
    from app.game.routes import game
    from app.commands import commands

    app.register_blueprint(game, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(commands)

    return app
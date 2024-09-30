#!/usr/bin/env python
from flask import Flask
from flask_assets import Environment, Bundle
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app_settings = 'app.config.Config'
    app.config.from_object(app_settings)
    assets = Environment(app)
    assets.url = app.static_url_path
    scss = Bundle('scss/style.scss', 'scss/tiles.scss', filters='pyscss', output='css/all.css')
    assets.register('scss_all', scss)
    general = Bundle('scss/variables.scss', 'scss/navbar.scss',  filters='pyscss', output='css/general.css')
    assets.register('general', general)
    custom_scss = Bundle('scss/customs.scss', filters='pyscss', output='css/customs.css')
    assets.register('customs', custom_scss)

    home_scss = Bundle('scss/pages/home.scss', filters='pyscss', output='css/pages/home.css')
    assets.register('home_scss', home_scss)
    menu_scss = Bundle('scss/pages/menu.scss', filters='pyscss', output='css/pages/menu.css')
    assets.register('menu_scss', menu_scss)
    join_scss = Bundle('scss/pages/join_game.scss', filters='pyscss', output='css/pages/join_game.css')
    assets.register('join_scss', join_scss)
    waiting_room_scss = Bundle('scss/pages/waiting_room.scss', filters='pyscss', output='css/pages/waiting_room.css')
    assets.register('waiting_room_scss', waiting_room_scss)
    profile_scss = Bundle('scss/pages/profile.scss', filters='pyscss', output='css/pages/profile.css')
    assets.register('profile_scss', profile_scss)    

    js = Bundle('js/throttle.js', 'js/selectors.js', 'js/buildOnField.js', 'js/updateDisplay.js', output='js/build.js')
    assets.register('js_build', js)

    db.init_app(app)
    bcrypt.init_app(app)

    # MORE

    return app
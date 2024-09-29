#!/usr/bin/env python
from flask import Flask
from flask_assets import Environment, Bundle

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

    # MORE

    return app
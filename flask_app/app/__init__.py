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
    # MORE

    return app
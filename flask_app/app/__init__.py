#!/usr/bin/env python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app_settings = 'app.config.Config'
    app.config.from_object(app_settings)

    # MORE

    return app
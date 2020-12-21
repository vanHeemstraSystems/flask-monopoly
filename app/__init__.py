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

    assets = Environment(app)
    assets.url = app.static_url_path
    scss = Bundle('scss/style.scss', 'scss/tiles.scss', filters='pyscss', output='css/all.css')
    assets.register('scss_all', scss)
    js = Bundle('js/updateDisplay.js', output='js/build.js')
    assets.register('js_build', js)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'


    from app.routes import routes

    app.register_blueprint(routes, url_prefix='/')

    return app

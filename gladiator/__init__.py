import os

import dotenv
from flask import Flask

from . import gladiator

dotenv.load_dotenv()


def create_app(test_config=None):
    app = initialize_app(test_config)
    ensure_instance_folder_exists(app)
    register_blueprints(app)
    return app


def initialize_app(test_config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    load_app_config(app, test_config)
    return app


def load_app_config(app, test_config):
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


def ensure_instance_folder_exists(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def register_blueprints(app):
    app.register_blueprint(gladiator.bp)
    app.add_url_rule('/', endpoint='index')

import os
from flask import Flask

from flask_restx.apidoc import apidoc

from flask_jwt_extended import JWTManager


from decouple import config


ROOT_URL = '/sample_project'


def create_app(config_name):
    
    from backend.config import app_config

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["APPLICATION_ROOT"] = ROOT_URL
    
    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = config("JWT_SECRET_KEY")
    jwt = JWTManager(app)


    with app.app_context():
        from backend.api_v1 import blueprint as api
        from backend.healthcheck import healthcheck

        app.register_blueprint(api, url_prefix=ROOT_URL + '/api/v1.0')
        app.register_blueprint(healthcheck, url_prefix=ROOT_URL + '/version')
    return app

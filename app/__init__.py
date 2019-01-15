from flask import Flask, Blueprint

import os

from config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])

    from app.api.v1 import v1
    app.register_blueprint(v1)

    @app.errorhandler(400)
    def handle_bad_request(error):
        """ Handles 400 errors """
        return 'Bad Request!', 400
    
    @app.errorhandler(404)
    def handle_not_found(error):
        """ handles 404 eroors """
        return 'Not Found!', 404


    return app
from flask import Flask
from views import admin
from app_logger import logger


def create_app():
    # here the env info or config info can be passed in
    # to create the app

    app = Flask(__name__)
    app.register_blueprint(admin)
    logger.info('Created!', extra={'well': ''})
    return app

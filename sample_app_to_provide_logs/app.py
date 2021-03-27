from flask import Flask
from bluerprints.basic_views import front_page
from logging.config import dictConfig


def create_app():
    # here the env info or config info can be passed in
    # to create the app

    dictConfig(
        {
            "version": 1,
            "formatters": {"json": {"()": "pythonjsonlogger.jsonlogger.JsonFormatter"}},
            "handlers": {
                "console": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "json",
                },
            },
            "root": {"level": "INFO", "handlers": ["console"]},
        }
    )
    app = Flask(__name__)
    app.register_blueprint(front_page)

    return app

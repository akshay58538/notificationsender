import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from healthifyme.notifications.config.provider import ConfigProvider


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = ConfigProvider().getMySqlConfig().get('url')
    # Configure application logger here
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    return app


def http_error(e):
    return jsonify(dict(error=e.description, message=e.message)), e.code


def generic_error(e):
    app.logger.exception("unknown failure")
    return jsonify(dict(error='unknown failure', message=e.message)), 500


app = create_app()
db = SQLAlchemy(app)

app.register_error_handler(405, http_error)
app.register_error_handler(401, http_error)
app.register_error_handler(403, http_error)
app.register_error_handler(Exception, generic_error)


if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()

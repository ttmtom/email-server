import os
from flask import Flask
from flask_mail import Mail


def create_app():
    app = Flask(__name__)

    mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": os.environ.get('SERVER_MAIL_ADDRESS'),
        "MAIL_PASSWORD": os.environ.get('SERVER_MAIL_PASSWORD'),
    }
    app.config.update(mail_settings)
    mail = Mail(app)

    from app.api import api_setup
    api = api_setup(mail)
    api.init_app(app)

    return app

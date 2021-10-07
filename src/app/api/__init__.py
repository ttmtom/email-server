from flask_restx import Api
from app.api.server.controller import setup_system_ns
from app.api.mail.controller import setup_mail_ns
from app.constants.path import MAIL_SERVICES_PATH, SERVER_SERVICES_PATH


def api_setup(flask_mail):
    api = Api()

    ns_server = setup_system_ns()
    api.add_namespace(ns_server, path=SERVER_SERVICES_PATH)

    ns_email = setup_mail_ns(flask_mail)
    api.add_namespace(ns_email, path=MAIL_SERVICES_PATH)

    return api
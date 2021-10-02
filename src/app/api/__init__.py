from flask_restx import Api
from app.api.server.controller import app as ns_server
from app.api.mail.controller import app as ns_email
from app.constants.path import MAIL_SERVICES_PATH, SERVER_SERVICES_PATH

api = Api()
api.add_namespace(ns_server, path=SERVER_SERVICES_PATH)
api.add_namespace(ns_email, path=MAIL_SERVICES_PATH)

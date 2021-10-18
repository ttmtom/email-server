from flask_restx import Namespace
from app.constants.path import SERVER_SERVICES_PATH


class ServerDto:
    api = Namespace(SERVER_SERVICES_PATH, description='server services')

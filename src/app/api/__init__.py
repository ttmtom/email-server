from flask_restx import Api
from app.api.server.controller import app as ns_server

api = Api()
api.add_namespace(ns_server, path='/server')

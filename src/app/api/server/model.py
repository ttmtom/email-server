from flask_restx import fields

class Model():
    def __init__(self, api) -> None:
        self.pingModel = api.model('PingServerS', {
            'msg': fields.String,
        })

from flask_restx import fields

class Model():
    def __init__(self, api) -> None:
        self.sendSuccessModel = api.model('Succcess', {
            'success': fields.Boolean,
        })

        self.badArgsMode = api.model('BadArgs', {
            'success': fields.Boolean,
        })

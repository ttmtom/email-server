from flask_restx import Resource
from app.api.server.model import Model
from app.api.server.serverDto import ServerDto

def setup_system_ns():
    app = ServerDto.api
    apiModel = Model(app)


    @app.route('/pingSystem', methods=['GET', 'POST'])
    @app.response(200, 'Success', apiModel.pingModel)
    class Server(Resource):
        def get(self):
            return {
                'msg': 'get hello world!'
            }

        def post(self):
            return {
                'msg': 'post hello world!'
            }

    return app
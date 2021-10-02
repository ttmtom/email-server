from flask_restx import Namespace, Resource, namespace
from app.api.server.model import Model
from app.constants.path import SERVER_SERVICES_PATH

app = Namespace(SERVER_SERVICES_PATH, description='server')
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

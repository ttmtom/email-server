from flask_restx import Namespace, Resource
from app.api.model import Model

app = Namespace('/server', description='server')
apiModel = Model(app)

@app.route('/ping')
class Server(Resource):
    @app.response(200, 'Success', apiModel.pingModel)
    def get(self):
        return {
            'msg': 'hello world'
        }
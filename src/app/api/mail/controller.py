from flask_restx import Namespace, Resource, reqparse
from app.api.mail.service import sendEmail
from app.constants.path import MAIL_SERVICES_PATH
from app.api.mail.model import Model

def setup_mail_ns (flask_mail):
    app = Namespace(MAIL_SERVICES_PATH, description='mail services')
    apiModel = Model(app)

    @app.route('/send', methods=['POST'])
    class Server(Resource):
        @app.response(200, 'Success', apiModel.sendSuccessModel)
        @app.response(400, 'Bad args', apiModel.badArgsMode)
        @app.doc(params={'target': 'target email address'})
        def post(self):
            print('post send email')
            parser = reqparse.RequestParser()
            parser.add_argument('target', type=str, required=True,  help='target email address')
            args = parser.parse_args()

            print(args)
            sendEmail(args.target, 'hii')

            return {
                'success': True
            }

    return app

# from flask import request
from flask_restx import Resource, reqparse
from flask import request
from flask_restx.fields import String
from app.api.mail.service import sendEmail
from app.api.mail.model import Model
from app.api.mail.mailDto import MailDto

def setup_mail_ns (flask, flask_mail):
    app = MailDto.api
    apiModel = Model(app)
    _mail = MailDto.mail
    # request_model = flask.schema_model('mail_quest', MailDto.mail)

    @app.route('/send', methods=['POST'])
    class Server(Resource):
        @app.response(200, 'Success', apiModel.sendSuccessModel)
        @app.response(400, 'Bad args', apiModel.badArgsMode)
        @app.expect(_mail, validate=True)
        def post(self):
            print('post send email')

            data = request.json
            print('-------------hiii')
            print(data)
            print(data['target'])

            sendEmail(flask_mail, data['target'], data['content'])

            return {
                'success': True
            }

    return app

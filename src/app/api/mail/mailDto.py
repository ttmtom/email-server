from flask_restx import Namespace, fields
from app.constants.path import MAIL_SERVICES_PATH


class MailDto:
    api = Namespace(MAIL_SERVICES_PATH, description='mail services')
    mail = api.model('mail', {
        'target': fields.String(Required=True, description='target mail address'),
        'content': fields.String(Required=True, description='content'),
        'title': fields.String(Required=True, description='mail title')
    })

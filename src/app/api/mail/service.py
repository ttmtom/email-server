import os
from flask_mail import Message

def sendEmail (flask_mail, mail: str, content: str):
    print(os.environ.get('SERVER_MAIL_ADDRESS'))
    print('send mail to ' + mail)
    print('content: ' + content)

    msg = Message(
        subject='testing',
        sender=os.environ.get('SERVER_MAIL_ADDRESS'),
        recipients=[mail],
        body=content,
        )

    flask_mail.send(msg)

    return {
        'success': True,
    }


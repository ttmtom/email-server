import os

def sendEmail (flask_mail, mail: str, content: str):
    print(os.environ.get('SERVER_MAIL_ADDRESS'))
    print('send mail to ' + mail)
    print('content: ' + content)
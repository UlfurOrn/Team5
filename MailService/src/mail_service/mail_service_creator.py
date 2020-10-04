
class MailServiceCreator:

    def __init__(self, mail_service):
        self.mail_service = mail_service()

    def get_mail_service(self):
        return self.mail_service

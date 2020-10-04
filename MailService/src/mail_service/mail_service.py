from mail_service.mail_service_interface import MailServiceInterface
from mail_service.mail_service_sendgrid import MailServiceSendgrid


class MailService(MailServiceInterface):

    def __init__(self, mail_service):
        self.mail_service = mail_service()

    def send_email(self, emails):
        self.mail_service.send_email(emails)

    def get_mail(self):
        return self.mail_service.get_mail()

    def get_subject(self):
        return self.mail_service.get_subject()

    def set_subject(self, subject):
        self.mail_service.set_subject(subject)

    def get_content(self):
        return self.mail_service.get_content()

    def set_content(self, content):
        self.mail_service.set_content(content)


mail_service = MailService(MailServiceSendgrid)

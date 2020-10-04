from abc import ABC


class MailServiceInterface(ABC):

    @classmethod
    def send_email(cls, emails):
        pass

    @classmethod
    def get_mail(cls):
        pass

    @classmethod
    def get_subject(cls):
        pass

    @classmethod
    def set_subject(cls, subject):
        pass

    @classmethod
    def get_content(cls):
        pass

    @classmethod
    def set_content(cls, content):
        pass

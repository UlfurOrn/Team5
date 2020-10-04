from mail_service.mail_service_interface import MailServiceInterface


class MailServiceStub(MailServiceInterface):

    FROM_EMAIL = "my.habit.tracker.app@gmail.com"
    MESSAGE = {
        "from_email": FROM_EMAIL,
        "to_emails": "",
        "subject": "subject",
        "content": "content"
    }

    def send_email(self, emails):
        pass  # Replace with logging later

    def get_mail(self):
        return {
            "subject": self.MESSAGE["subject"],
            "content": self.MESSAGE["content"]
        }

    def get_subject(self):
        return {"subject": self.MESSAGE["subject"]}

    def set_subject(self, subject):
        self.MESSAGE["subject"] = subject

    def get_content(self):
        return {"content": self.MESSAGE["content"]}

    def set_content(self, content):
        self.MESSAGE["content"] = content

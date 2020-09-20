
class MailServiceStub:

    FROM_EMAIL = "my.habit.tracker.app@gmail.com"
    MESSAGE = {
        "from_email": FROM_EMAIL,
        "to_emails": "",
        "subject": "subject",
        "content": "content"
    }

    def send_email(self, emails):
        pass

    def get_subject(self):
        return {"subject": self.MESSAGE["subject"]}

    def set_subject(self, subject):
        self.MESSAGE[subject] = subject

    def get_content(self):
        return {"content": self.MESSAGE["content"]}

    def set_content(self, content):
        self.MESSAGE["content"] = content

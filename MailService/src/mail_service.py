import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class MailService:

    API_KEY = "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"
    FROM_EMAIL = "my.habit.tracker.app@gmail.com"
    MESSAGE = Mail(
            from_email=FROM_EMAIL,
            to_emails=[],
            subject="",
            html_content=""
        )

    def send_email(self, emails):
        # Make secure if needed
        api_key = self.API_KEY
        sg = SendGridAPIClient(api_key)

        message = self.MESSAGE
        message.to = emails
        sg.send(message)

    def get_subject(self):
        return self.MESSAGE.subject

    def set_subject(self, subject):
        self.MESSAGE.subject = subject

    def get_content(self):
        return self.MESSAGE.content

    def set_content(self, content):
        self.MESSAGE.content = content


mail_service = MailService()

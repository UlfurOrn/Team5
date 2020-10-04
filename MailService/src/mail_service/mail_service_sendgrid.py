import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from mail_service.mail_service_interface import MailServiceInterface


class MailServiceSendgrid(MailServiceInterface):

    API_KEY = os.environ.get("SENDGRID_API_KEY")
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

    def get_mail(self):
        subject = self.MESSAGE.subject
        content = self.MESSAGE.contents[0]
        content = content.get()["value"]

        return {
            "subject": subject,
            "content": content
        }

    def get_subject(self):
        return self.MESSAGE.subject

    def set_subject(self, subject):
        self.MESSAGE.subject = subject

    def get_content(self):
        return self.MESSAGE.contents[0]

    def set_content(self, content):
        self.MESSAGE._contents = None  # Could not find better solution, no clear method
        self.MESSAGE.content = content

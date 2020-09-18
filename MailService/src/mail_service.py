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

    def send_email(self, email):
        # Make secure if needed
        api_key = self.API_KEY
        sg = SendGridAPIClient(api_key)

        message = self.MESSAGE
        message.to = email
        sg.send(message)

    def change_subject(self, subject):
        self.MESSAGE.subject = subject

    def change_content(self, content):
        self.MESSAGE.content = content


if __name__ == "__main__":
    ms = MailService()

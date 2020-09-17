import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class MailService:

    def send_email(self):
        message = Mail(
            from_email="my.habit.tracker.app@gmail.com",
            to_emails="ulfurinn@gmail.com",
            subject="Mail Service",
            html_content="Bjó til email service fyrir Sprintinn lol"
        )

        # Make secure if needed
        api_key = "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"
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)

        print(response.status_code)
        print(response.body)
        print(response.headers)


if __name__ == "__main__":
    ms = MailService()
    ms.send_email()

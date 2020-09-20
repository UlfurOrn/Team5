from flask import request
from flask_restplus import Resource

from models.email_dto import EmailDTO
from mail_service import MailService

api = EmailDTO.api
email_model = EmailDTO.model


@api.route('')
class EmailEndpoint(Resource):
    @api.marshal_with(email_model)
    def get(self):
        """View subject and content of the email"""

        mail_service = MailService()
        return mail_service.get_mail()

    @api.expect(email_model, validate=True)
    @api.marshal_with(email_model)
    def post(self):
        """Send email"""

        data = request.json
        emails = data["emails"]

        return # mail_service.send_email(emails)

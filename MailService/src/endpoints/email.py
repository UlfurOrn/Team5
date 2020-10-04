from flask import request
from flask_restplus import Resource

from models.email_dto import EmailDTO
from mail_service.mail_service import mail_service

api = EmailDTO.api
email_model = EmailDTO.model
email_expect = EmailDTO.expect


@api.route('')
class EmailEndpoint(Resource):
    @api.marshal_with(email_model)
    def get(self):
        """View subject and content of the email"""
        return mail_service.get_email()

    @api.expect(email_expect, validate=True)
    def post(self):
        """Send email"""

        data = request.json
        emails = data["emails"]

        try:
            mail_service.send_email(emails)
        except Exception as e:
            return str(e), 503

        return "", 200

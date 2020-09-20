from flask import request
from flask_restplus import Resource

from models.subject_dto import SubjectDTO
from mail_service import MailService

api = SubjectDTO.api
subject_model = SubjectDTO.model


@api.route('')
class SubjectEndpoint(Resource):
    @api.marshal_with(subject_model)
    def get(self):
        """Get subject of email"""

        mail_service = MailService()
        return mail_service.get_subject()

    @api.expect(subject_model, validate=True)
    @api.marshal_with(subject_model)
    def put(self):
        """Change subject of email"""

        data = request.json
        subject = data["subject"]

        mail_service = MailService()
        mail_service.set_subject(subject)
        return mail_service.get_subject()

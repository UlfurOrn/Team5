from flask import request
from flask_restplus import Resource

from models.content_dto import ContentDTO
from mail_service import MailService

api = ContentDTO.api
content_model = ContentDTO.model


@api.route('')
class ContentEndpoint(Resource):
    @api.marshal_with(content_model)
    def get(self):
        """Get content of email"""

        mail_service = MailService()
        return mail_service.get_content()

    @api.expect(content_model, validate=True)
    @api.marshal_with(content_model)
    def put(self):
        """Change content of email"""

        data = request.json
        content = data["content"]

        mail_service = MailService()
        mail_service.set_content(content)
        return mail_service.get_content()

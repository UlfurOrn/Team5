from flask_restplus import Namespace, fields


class ContentDTO:
    api = Namespace('content', description='Get and Change content of email')
    model = api.model('Content', {
        'content': fields.String(required=True, description='Content of the email', example="Content")
    })

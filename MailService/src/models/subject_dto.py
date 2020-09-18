from flask_restplus import Namespace, fields


class SubjectDTO:
    api = Namespace('subject', description='Get and Change subject of email')
    model = api.model('Subject', {
        'subject': fields.String(required=True, description='Subject of the email', example="Subject")
    })

from flask_restplus import Namespace, fields


class EmailDTO:
    api = Namespace('email', description='Send and View emails')
    model = api.model('Email', {
        'subject': fields.String(required=True, description='Subject of the email', example="Subject"),
        'content': fields.String(required=True, description='Content of the email', example="Content")
    })
    expect = api.model('To emails', {
        'emails': fields.List(
            fields.String(required=True, description="List of user emails", example="user1@email.com")
        )
    })

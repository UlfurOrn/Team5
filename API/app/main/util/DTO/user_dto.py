from flask_restplus import Namespace, fields


class UserDTO:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'name': fields.String(required=True, description='The name of the user'),
        'email': fields.String(required=True, description='The email of the user'),
        'dob': fields.Date(required=True, description='The date of birth of the user'),
        'username': fields.String(required=False, description='Username'),
        'password': fields.String(required=False, description='Password'),
        'gender': fields.String(required=True, description='The gender of the user'),
        'weight': fields.Integer(required=True, description='The users weight'),
        'height': fields.Integer(required=True, description='The users height'),
    })
    output_user = api.inherit("user out", user, {
        'userid': fields.Integer(required=True, description='The user identification number for the user')
    })

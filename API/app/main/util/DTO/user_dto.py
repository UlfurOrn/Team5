from flask_restplus import Namespace, fields

class UserDTO:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
       'Name': fields.String(required=True, description='The name of the user'),
       'Email': fields.String(required=True, description='The email of the user'),
       'DoB': fields.DateTime(required=True, description='The date of birth of the user'),
       'Gender': fields.String(required=True, description='The gender of the user'),
       'Weight': fields.Integer(required=True, description='The users weight'),
       'Height': fields.Integer(required=True, description='The users height'),
    })

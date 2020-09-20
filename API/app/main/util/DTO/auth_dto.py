from flask_restplus import Namespace, fields

class AuthDTO:
    api = Namespace('auth', description='Authendication related operations')
    auth =  api.model('auth', {
        'username': fields.String(required=True, description='User username'),
        'password': fields.String(required=True, description='User passsword') 
    })

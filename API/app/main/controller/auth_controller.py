from flask import request
from flask_restplus import Resource, Namespace

from main.repositories.users_io import Usersio
from main.util.DTO.auth_dto import AuthDTO

api = AuthDTO.api
_auth = AuthDTO.auth

@api.route('/login')
class UserLogin(Resource):
    @api.doc('User login')
    @api.expect(_auth, validate=True)
    def post(self):
        '''Uses the Userio.password() function to check if the 
        username and password match.

        Returns:
            tuple: response message and conde
        '''
        post_data = request.json

        if Usersio.password(post_data['username'], post_data['password']):
            return "successfully logged in", 200
        else:
            return "", 404
        
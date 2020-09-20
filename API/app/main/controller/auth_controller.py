from flask import request
from flask_restplus import Resource, Namespace

from main.services.db_api import DBapi
# from main.repositories.users_io import Usersio
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
            tuple: response message and code
        '''
        post_data = request.json

        pass_resp = DBapi.checkpassword(post_data['username'], post_data['password'])

        if pass_resp[0][0]:
            return "successfully logged in", 200
        else:
            return "couldn't log in", 404
        
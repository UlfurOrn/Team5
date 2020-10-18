from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import Unauthorized, Forbidden

from main.services.db_api import DBapi
from main.util.DTO.auth_dto import AuthDTO
from main.util.DTO.error_message import error_message

api = AuthDTO.api
_auth = AuthDTO.auth


@api.response("Unauthorized", 401, error_message)
@api.response("Forbidden", 403, error_message)
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

        username = post_data["username"]
        password = post_data["password"]

        # If both fields are emtpy strings
        if not (username or password):
            raise Unauthorized("Missing username and password")

        pass_resp = DBapi.users.checkpassword(username, password)

        if pass_resp[0][0]:
            return "successfully logged in", 200
        else:
            raise Forbidden("Invalid username or password")

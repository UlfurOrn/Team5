from flask import request
from flask_restplus import Resource
from main.services.db_api import DBapi

from main.util.DTO.user_dto import UserDTO

api = UserDTO.api
_user = UserDTO.user


@api.route('')
class UserList(Resource):
    @api.doc('List all users')
    @api.marshal_list_with(_user, envelope='users')
    def get(self):
        data = DBapi.users('GET')

        user_list = []
        for user in data:
            user_list.append(dict(user))

        return user_list

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return DBapi.users('POST', data=data)


@api.route('/<user_id>')
@api.response(404, 'User not found.')
class SingleUser(Resource):
    @api.doc('Get a single user')
    @api.marshal_with(_user)
    def get(self, user_id):
        data = DBapi.users('GET', user_id)
        user_dict = dict(data[0])
        return user_dict

    @api.response(201, 'User successfully updated.')
    @api.doc('Edit a user')
    @api.expect(_user)
    def put(self, user_id):
        data = request.json
        return DBapi.users('PUT', user_id, data)

    @api.doc('Delete a user')
    @api.response(201, 'user successfully deleted.')
    def delete(self, user_id):
        return DBapi.users('DELETE', user_id)

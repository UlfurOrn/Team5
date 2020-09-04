from flask import request
from flask_restplus import Resource
from ..services.dbapi import DBapi

from ..util.DTO.userDTO import UserDTO

api = UserDTO.api
_user = UserDTO.user

@api.route('/user')
class UserList(Resource):
    @api.doc('List all users')
    @api.marhal_list_with(_user, envelope='users')
    def get(self):
        return DBapi.users('GET')

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return DBapi.users('POST', data=data)


@api.route('/user/<id>')
@api.response(404, 'User not found.')
class user(Resource):
    @api.doc('Get a single user')
    def get(self):
        return DBapi('GET', id)

    @api.response(201, 'User successfully updated.')
    @api.doc('Edit a user')
    def put(self):
        data = request.json
        return DBapi('PUT', id, data)

    @api.doc('Delete a user')
    @api.response(201, 'user successfully deleted.')
    def delete(self):
        return DBapi('DELETE', id)

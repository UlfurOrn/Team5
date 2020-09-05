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
        return DBapi.users('GET')

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return DBapi.users('POST', data=data)


@api.route('/<id>')
@api.response(404, 'User not found.')
class user(Resource):
    @api.doc('Get a single user')
    @api.marshal_with(_user)
    def get(self, id):
        print("Start")
        data = DBapi.users('GET', id)
        print("Done")
        print(dict(data[0]))
        return dict(data[0])

    @api.response(201, 'User successfully updated.')
    @api.doc('Edit a user')
    def put(self):
        data = request.json
        return DBapi.users('PUT', id, data)

    @api.doc('Delete a user')
    @api.response(201, 'user successfully deleted.')
    def delete(self):
        return DBapi.users('DELETE', id)

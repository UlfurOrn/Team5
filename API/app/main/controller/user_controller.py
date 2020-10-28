from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest, NotFound

from main.util.logging.logging_registry import LoggingRegistry
from main.util.authentication.authentication_test import AuthTest

from main.util.DTO.error_message import error_message
from main.util.mappers.usermapper import UserMapper
from main.services.db_api import DBapi
from main.util.DTO.user_dto import UserDTO
from main.util.DTO.habit_dto import HabitDTO
from main.util.DTO.record_dto import RecordDTO

logger = LoggingRegistry.get_logger()
api = UserDTO.api
_expect = UserDTO.expected_model
_user = UserDTO.model
_habit = HabitDTO.model
_record = RecordDTO.model


@api.route('')
class UserList(Resource):
    @api.doc('List all users')
    @api.marshal_list_with(_user, envelope='users')
    def get(self):
        data = DBapi.users.get()

        user_list = []
        for user in data:
            user_list.append(user.to_dict())

        return user_list

    @api.response(201, 'User successfully created.')
    @api.response(400, 'Invalid Password', error_message)
    @api.doc('create a new user')
    @api.expect(_expect, validate=True)
    def post(self):
        data = request.json

        password = data["password"]
        if not AuthTest.valid_password(password):
            raise BadRequest("Password not secure")

        user = UserMapper()
        user.set_dict(data)
        return DBapi.users.post(user)


@api.route('/<int:user_id>')
@api.response(400, "BadRequest", error_message)
@api.response(404, 'User not found.', error_message)
class SingleUser(Resource):
    @api.doc('Get a single user')
    @api.marshal_with(_user)
    def get(self, user_id):
        check_id(user_id)

        data = DBapi.users.get(user_id)
        user_dict = data[0].to_dict()
        return user_dict

    @api.doc('Edit a user')
    @api.response(201, 'User successfully updated.')
    @api.expect(_expect)
    def put(self, user_id):
        check_id(user_id)

        data = request.json
        user = UserMapper()
        user.set_dict(data)
        DBapi.users.put(user_id, user)

        return DBapi.users.get(user_id)[0].to_dict(), 201

    @api.doc('Delete a user')
    @api.response(200, 'User successfully deleted.')
    def delete(self, user_id):
        check_id(user_id)

        DBapi.users.delete(user_id)
        return "", 200


@api.route("/<int:user_id>/habit")
@api.response(400, "BadRequest", error_message)
@api.response(404, 'User not found.', error_message)
class UserHabits(Resource):

    @api.marshal_list_with(_habit, envelope='habits')
    def get(self, user_id):
        check_id(user_id)

        data = DBapi.habits.get(user_id=user_id)

        habit_list = []
        for habit in data:
            habit_list.append(habit.to_dict())

        return habit_list


@api.route("/<int:user_id>/record")
@api.response(400, "BadRequest", error_message)
@api.response(404, 'User not found.', error_message)
class UserRecords(Resource):

    @api.marshal_list_with(_record, envelope='records')
    def get(self, user_id):
        check_id(user_id)

        data = DBapi.records.get(user_id=user_id)

        record_list = []
        for record in data:
            record_list.append(record.to_dict())

        return record_list


def check_id(user_id):
    if user_id <= 0:
        raise BadRequest("User id must be higher than 0")
    if not DBapi.users.get(user_id):
        raise NotFound(f"User with id {user_id} not found")

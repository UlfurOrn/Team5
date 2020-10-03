from flask import request
from flask_restplus import Resource

from main.util.logging.logging_registry import LoggingRegistry

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
        data = DBapi.users('GET')

        user_list = []
        for user in data:
            user_list.append(user.to_dict())

        return user_list

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_expect, validate=True)
    def post(self):
        data = request.json
        user = UserMapper()
        user.set_dict(data)
        return DBapi.users('POST', data=user)


@api.route("/<user_id>/habit")
class UserHabit(Resource):

    @api.marshal_list_with(_habit, envelope='habits')
    def get(self, user_id):
        data = DBapi.habits("GET")

        habit_list = []
        for habit in data:
            habit_dict = habit.to_dict()
            if habit_dict["userid"] == int(user_id):
                habit_list.append(habit_dict)

        return habit_list


@api.route("/<user_id>/record")
class UserRecords(Resource):

    @api.marshal_list_with(_record, envelope='records')
    def get(self, user_id):
        data = DBapi.records("GET")

        record_list = []
        for record in data:
            record_dict = record.to_dict()
            if record_dict["userid"] == int(user_id):
                record_list.append(record_dict)

        return record_list


@api.route('/<user_id>')
@api.response(404, 'User not found.')
class SingleUser(Resource):
    @api.doc('Get a single user')
    @api.marshal_with(_user)
    def get(self, user_id):
        data = DBapi.users('GET', user_id)
        if not data:
            return "", 404
        user_dict = data[0].to_dict()
        return user_dict

    @api.response(201, 'User successfully updated.')
    @api.doc('Edit a user')
    @api.expect(_expect)
    def put(self, user_id):
        data = request.json
        user = UserMapper()
        user.set_dict(data)
        return DBapi.users('PUT', user_id, data=user)

    @api.doc('Delete a user')
    @api.response(201, 'user successfully deleted.')
    def delete(self, user_id):
        return DBapi.users('DELETE', user_id)

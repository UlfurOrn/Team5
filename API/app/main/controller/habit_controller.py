from flask import request
from flask_restplus import Resource
from main.services.db_api import DBapi

from main.util.DTO.habit_dto import HabitDTO

api = HabitDTO.api
_habit = HabitDTO.habit


@api.route('')
class HabitList(Resource):
    @api.doc('List all habits')
    @api.marshal_list_with(_habit, envelope='habits')
    def get(self):
        data = DBapi.habits('GET')

        record_list = []
        for record in data:
            record_list.append(dict(record))

        return record_list

    @api.response(201, 'Habit successfully created.')
    @api.doc('create a new Habit')
    @api.expect(_habit, validate=True)
    def post(self):
        data = request.json
        return DBapi.habits('POST', data=data)


@api.route('/<habit_id>')
@api.response(404, 'Habit not found.')
class SingleHabit(Resource):
    @api.doc('Get a single habit')
    @api.marshal_with(_habit)
    def get(self, habit_id):
        data = DBapi.habits('GET', habit_id)
        habit_dict = dict(data[0])
        return habit_dict

    @api.response(201, 'Habit successfully updated.')
    @api.doc('Edit a habit')
    @api.expect(_habit, validate=True)
    def put(self, habit_id):
        data = request.json
        return DBapi.habits('PUT', habit_id, data=data)

    @api.doc('Delete a habit')
    @api.response(201, 'Habit successfully deleted.')
    def delete(self, habit_id):
        return DBapi.habits('DELETE', habit_id)

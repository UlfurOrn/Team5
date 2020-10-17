from flask import request
from flask_restplus import Resource

from main.util.mappers.habitmapper import HabitMapper
from main.util.DTO.habit_dto import HabitDTO
from main.util.DTO.record_dto import RecordDTO
from main.services.db_api import DBapi

api = HabitDTO.api
_habit = HabitDTO.model


@api.route('')
class HabitList(Resource):
    @api.doc('List all measurements')
    @api.marshal_list_with(_habit, envelope='habits')
    def get(self):
        data = DBapi.habits.get()

        habit_list = []
        for habit in data:
            habit_list.append(habit.to_dict())

        return habit_list


@api.route('/<measurement_id>')
@api.response(404, 'Habit not found.')
class SingleHabit(Resource):
    @api.doc('Get a single habit')
    @api.marshal_with(_habit)
    def get(self, habit_id):
        data = DBapi.habits.get(habit_id)
        if not data:
            return "", 404
        habit_dict = data[0].to_dict()
        return habit_dict

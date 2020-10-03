from flask import request
from flask_restplus import Resource

from main.util.mappers.habitmapper import HabitMapper
from main.util.DTO.habit_dto import HabitDTO
from main.services.db_api import DBapi

api = HabitDTO.api
_expect = HabitDTO.expect_model
_habit = HabitDTO.model

@api.route('')
class HabitList(Resource):
    @api.doc('List all habits')
    @api.marshal_list_with(_habit, envelope='habits')
    def get(self):
        data = DBapi.habits.get()

        habit_list = []
        for habit in data:
            habit_list.append(habit.to_dict())

        return habit_list

    @api.response(201, 'Habit successfully created.')
    @api.doc('create a new Habit')
    @api.expect(_expect, validate=True)
    def post(self):
        data = request.json
        habit = HabitMapper()
        habit.set_dict(data)
        return DBapi.habits.post(habit)


@api.route('/<habit_id>')
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

    @api.response(201, 'Habit successfully updated.')
    @api.doc('Edit a habit')
    @api.expect(_expect, validate=True)
    def put(self, habit_id):
        data = request.json
        habit = HabitMapper()
        habit.set_dict(data)
        return DBapi.habits.put(habit_id, habit)

    @api.doc('Delete a habit')
    @api.response(201, 'Habit successfully deleted.')
    def delete(self, habit_id):
        return DBapi.habits.delete(habit_id)

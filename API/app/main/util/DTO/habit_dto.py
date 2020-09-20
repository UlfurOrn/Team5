from flask_restplus import Namespace, fields


class HabitDTO:
    api = Namespace('habit', description='Habit related operations')
    habit = api.model('habit', {
        'name': fields.String(required=True, description='The name of the habit'),
        'description': fields.String(required=True, description='Short description for the habit'),
        'measurement': fields.String('Measurement for the amount of a record of this habit')
    })

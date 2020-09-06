from flask_restplus import Namespace, fields


class TypeDTO:
    api = Namespace('type', description='Type related operations')
    type = api.model('type', {
        'name': fields.String(required=True, description='The name of the type'),
        'description': fields.String(required=True, description='Short description for the type'),
        'measurement': fields.String('Measurement for the amount of a record of this type')
    })

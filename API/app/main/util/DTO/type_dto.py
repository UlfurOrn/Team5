from flask_restplus import Namespace, fields


class TypeDTO:
    api = Namespace('type', description='Type related operations')
    type = api.model('type', {
        'Name': fields.String(required=True, description='The name of the type'),
        'Description': fields.String(required=True, description='Short description for the type'),
        'Measurement': fields.String('Measurement for the amount of a record of this type')
    })

from flask_restplus import Namespace, fields


class RecordDTO:
    api = Namespace('record', description='Record related operations')
    record = api.model('record', {
        'userid': fields.Integer(required=True, description='The user identification number for the record'),
        'typeid': fields.Integer(required=True, description='The type identifier for the record'),
        'rdatetime': fields.DateTime(required=True, description='The timestamp for the record'),
        'amount': fields.Float(required=True, description='The amount for the record')
    })

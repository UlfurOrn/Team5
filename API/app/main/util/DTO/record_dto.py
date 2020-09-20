from flask_restplus import Namespace, fields


class RecordDTO:
    api = Namespace('record', description='Record related operations')
    record = api.model('record', {
        'recordid': fields.Integer(description='The record identification number'),
        'userid': fields.Integer(required=True, description='The user identification number for the record'),
        'habitid': fields.Integer(required=True, description='The habit identifier for the record'),
        'rdate': fields.DateTime(required=True, description='The timestamp for the record'),
        'amount': fields.Float(required=True, description='The amount for the record')
    })

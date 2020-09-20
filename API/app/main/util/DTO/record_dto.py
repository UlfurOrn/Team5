from flask_restplus import Namespace, fields


class RecordDTO:
    api = Namespace('record', description='Record related operations')
    expect_model = api.model('Expected record', {
        'userid': fields.Integer(required=True, description='The user identification number for the record'),
        'habitid': fields.Integer(required=True, description='The habit identifier for the record'),
        'rdate': fields.DateTime(required=True, description='The timestamp for the record'),
        'amount': fields.Float(required=True, description='The amount for the record')
    })

    model = api.inherit("Record", expect_model, {
        "recordid": fields.Integer(required=True, description='The record identification number for the record')
    })

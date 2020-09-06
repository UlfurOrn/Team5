from flask_restplus import Namespace, fields

class RecordDTO:
    api = Namespace('record', description='Record related operations')
    record = api.model('record', {
        'UserId': fields.Integer(required=True, description='The user identification number for the record'),
        'TypeId': fields.Integer(required=True, description='The type identifier for the record'),
        'RDateTime': fields.DateTime(required=True, description='The tiestapm for the record'),
        'Amount': fields.Float(required=True, description='The amount for the record')
    })

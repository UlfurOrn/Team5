from flask_restplus import Namespace, fields


class MeasurementDTO:
    api = Namespace('measurement', description='Measurement related operations')
    model = api.model('Measurement', {
        "measurementid": fields.Integer(required=True, description='Measurement id'),
        "name": fields.String(required=True, description='Measurement name'),
        "abreviation": fields.String(required=True, description='Measurement name abreviation'),
        "mcategoryid": fields.Integer(required=True, description='Category id')
    })

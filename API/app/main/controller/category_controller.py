from flask import request
from flask_restplus import Resource

from main.util.mappers.mcategorymapper import McategoryMapper
from main.util.DTO.category_dto import CategoryDTO
from main.services.db_api import DBapi

api = McategoryDTO.api
_measurement = MeasurementDTO.model


@api.route('')
class MeasurementList(Resource):
    @api.doc('List all measurements')
    @api.marshal_list_with(_measurement, envelope='measurements')
    def get(self):
        data = DBapi.measurements.get()

        measurement_list = []
        for measurement in data:
            measurement_list.append(measurement.to_dict())

        return measurement_list


@api.route('/<measurement_id>')
@api.response(404, 'Measurement not found.')
class SingleMeasurement(Resource):
    @api.doc('Get a single measurement')
    @api.marshal_with(_measurement)
    def get(self, measurement_id):
        data = DBapi.measurements.get(measurement_id)
        if not data:
            return "", 404
        measurement_dict = data[0].to_dict()
        return measurement_dict

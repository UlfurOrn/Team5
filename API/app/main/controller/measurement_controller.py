from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest, NotFound

from main.util.DTO.error_message import error_message
from main.util.mappers.measurementmapper import MeasurementMapper
from main.util.DTO.measurement_dto import MeasurementDTO
from main.services.db_api import DBapi

api = MeasurementDTO.api
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


@api.route('/<int:measurement_id>')
@api.response(400, 'BadRequest', error_message)
@api.response(404, 'Measurement not found.', error_message)
class SingleMeasurement(Resource):
    @api.doc('Get a single measurement')
    @api.marshal_with(_measurement)
    def get(self, measurement_id):
        check_id(measurement_id)

        data = DBapi.measurements.get(measurement_id)
        measurement_dict = data[0].to_dict()
        return measurement_dict


def check_id(measurement_id):
    if measurement_id <= 0:
        raise BadRequest("Measurement id must be higher than 0")
    if not DBapi.measurements.get(measurement_id):
        raise NotFound(f"Measurement with id {measurement_id} not found")

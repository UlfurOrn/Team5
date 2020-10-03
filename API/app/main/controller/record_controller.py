from flask import request
from flask_restplus import Resource

from main.util.mappers.recordmapper import RecordMapper
from main.util.DTO.record_dto import RecordDTO
from main.services.db_api import DBapi
from main.services.pg_api import PGapi

api = RecordDTO.api
_expect = RecordDTO.expect_model
_record = RecordDTO.model

DBapi = DBapi(PGapi) # Initialize a new DBapi with PGapi as the database api

@api.route('')
class RecordList(Resource):
    @api.doc('List all records')
    @api.marshal_list_with(_record, envelope='records')
    def get(self):
        data = DBapi.records('GET')

        record_list = []
        for record in data:
            record_list.append(record.to_dict())

        return record_list

    @api.response(201, 'Type successfully created.')
    @api.doc('create a new Type')
    @api.expect(_expect, validate=True)
    def post(self):
        data = request.json
        record = RecordMapper()
        record.set_dict(data)
        print(record)
        return DBapi.records('POST', data=record)


@api.route('/<record_id>')
@api.response(404, 'Record not found.')
class SingleRecord(Resource):
    @api.doc('Get a single record')
    @api.marshal_with(_record)
    def get(self, record_id):
        data = DBapi.records('GET', record_id)
        if not data:
            return "", 404
        record_dict = data[0].to_dict()
        return record_dict

    @api.response(201, 'Record successfully updated.')
    @api.doc('Edit a record')
    @api.expect(_expect, validate=True)
    def put(self, record_id):
        data = request.json
        record = RecordMapper()
        record.set_dict(data)
        return DBapi.records('PUT', record_id, data=record)

    @api.doc('Delete a record')
    @api.response(201, 'Record successfully deleted.')
    def delete(self, record_id):
        return DBapi.records('DELETE', record_id)

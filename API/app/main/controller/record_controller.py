from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import NotFound

from main.util.DTO.error_message import error_message
from main.util.mappers.recordmapper import RecordMapper
from main.util.DTO.record_dto import RecordDTO
from main.services.db_api import DBapi

api = RecordDTO.api
_expect = RecordDTO.expect_model
_record = RecordDTO.model


@api.route('')
class RecordList(Resource):
    @api.doc('List all records')
    @api.marshal_list_with(_record, envelope='records')
    def get(self):
        data = DBapi.records.get()

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
        return DBapi.records.post(record)


@api.route('/<int:record_id>')
@api.response(404, 'Record not found.', error_message)
class SingleRecord(Resource):
    @api.doc('Get a single record')
    @api.marshal_with(_record)
    def get(self, record_id):
        data = DBapi.records.get(record_id)
        if not data:
            raise NotFound(f"Record with id {record_id} not found")
        record_dict = data[0].to_dict()
        return record_dict

    @api.response(201, 'Record successfully updated.')
    @api.doc('Edit a record')
    @api.marshal_with(_record)
    @api.expect(_expect, validate=True)
    def put(self, record_id):
        if not DBapi.records.get(record_id):
            raise NotFound(f"Record with id {record_id} not found")

        data = request.json
        record = RecordMapper()
        record.set_dict(data)
        DBapi.records.put(record_id, record)

        return DBapi.records.get(record_id)[0], 201

    @api.doc('Delete a record')
    @api.response(204, 'Record successfully deleted.')
    def delete(self, record_id):
        if not DBapi.records.get(record_id):
            raise NotFound(f"Record with id {record_id} not found")

        DBapi.records.delete(record_id)
        return "", 204

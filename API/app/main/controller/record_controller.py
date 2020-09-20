from flask import request
from flask_restplus import Resource

from main.util.mappers.record import Record
from main.util.DTO.record_dto import RecordDTO
from main.services.db_api import DBapi

api = RecordDTO.api
_expect = RecordDTO.record
_record = RecordDTO.output_record


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
        record = Record()
        record.set_dict(data)
        print(record)
        return DBapi.records('POST', data=record)


@api.route("/<user_id>")
class UserRecords(Resource):

    @api.marshal_list_with(_record, envelope='records')
    def get(self, user_id):
        data = DBapi.records("GET")

        record_list = []
        for record in data:
            record_dict = record.to_dict()
            if record_dict["userid"] == int(user_id):
                record_list.append(record_dict)

        return record_list


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
        record = Record()
        record.set_dict(data)
        return DBapi.records('PUT', record_id, data=record)

    @api.doc('Delete a record')
    @api.response(201, 'Record successfully deleted.')
    def delete(self, record_id):
        return DBapi.records('DELETE', record_id)

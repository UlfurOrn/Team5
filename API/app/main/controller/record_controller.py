from flask import request
from flask_restplus import Resource
from main.services.db_api import DBapi

from main.util.DTO.record_dto import RecordDTO

api = RecordDTO.api
_record = RecordDTO.record


@api.route('')
class RecordList(Resource):
    @api.doc('List all records')
    @api.marshal_list_with(_record, envelope='records')
    def get(self):
        data = DBapi.records('GET')

        record_list = []
        for record in data:
            record_list.append(dict(record))

        return record_list

    @api.response(201, 'Type successfully created.')
    @api.doc('create a new Type')
    @api.expect(_record, validate=True)
    def post(self):
        data = request.json
        return DBapi.records('POST', data=data)


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



@api.route('/<user_id>/<type_id>/<datetime>')
@api.response(404, 'Record not found.')
class Record(Resource):
    @api.doc('Get a single record')
    @api.marshal_with(_record)
    def get(self, user_id, type_id, datetime):
        data = DBapi.records('GET', [user_id, type_id, datetime])
        record_dict = dict(data[0])
        return record_dict

    @api.response(201, 'Record successfully updated.')
    @api.doc('Edit a record')
    @api.expect(_record, validate=True)
    def put(self, user_id, type_id, datetime):
        data = request.json
        return DBapi.records('PUT', [user_id, type_id, datetime], data=data)

    @api.doc('Delete a record')
    @api.response(201, 'Record successfully deleted.')
    def delete(self, user_id, type_id, datetime):
        return DBapi.records('DELETE', [user_id, type_id, datetime])

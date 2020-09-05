from flask import request
from flask_restplus import Resource
from main.services.db_api import DBapi

from main.util.DTO.record_dto import RecordDTO

api = RecordDTO.api
_record = RecordDTO.record

@api.route('/record')
class RecordList(Resource):
    @api.doc('List all records')
    @api.marshal_list_with(_record, envelope='records')
    def get(self):
        return DBapi.records('GET')

    @api.response(201, 'Type successfully created.')
    @api.doc('create a new Type')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return DBapi.types('POST',data=data)

@api.route('/record/<id>')
@api.response(404, 'Record not found.')
class Record(Resource):
    @api.doc('Get a single record')
    def get(self):
        return DBapi.records('GET',id)

    @api.response(201, 'Record successfully updated.')
    @api.doc('Edit a record')
    def put(self):
        data = request.json
        return DBapi('PUT',id,data)

    @api.doc('Delete a record')
    @api.response(201, 'Record successfully deleted.')
    def delete(self):
        return DBapi('DELETE',id)
    

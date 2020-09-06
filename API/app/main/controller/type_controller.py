from flask import request
from flask_restplus import Resource
from main.services.db_api import DBapi

from main.util.DTO.type_dto import TypeDTO

api = TypeDTO.api
_type = TypeDTO.type


@api.route('')
class TypeList(Resource):
    @api.doc('List all types')
    @api.marshal_list_with(_type, envelope='types')
    def get(self):
        data = DBapi.types('GET')

        record_list = []
        for record in data:
            record_list.append(dict(record))

        return record_list

    @api.response(201, 'Type successfully created.')
    @api.doc('create a new Type')
    @api.expect(_type, validate=True)
    def post(self):
        data = request.json
        return DBapi.types('POST', data=data)


@api.route('/<type_id>')
@api.response(404, 'Type not found.')
class SingleType(Resource):
    @api.doc('Get a single type')
    @api.marshal_with(_type)
    def get(self, type_id):
        data = DBapi.types('GET', type_id)
        type_dict = dict(data[0])
        return type_dict

    @api.response(201, 'Type successfully updated.')
    @api.doc('Edit a type')
    @api.expect(_type, validate=True)
    def put(self, type_id):
        data = request.json
        return DBapi.types('PUT', type_id, data=data)

    @api.doc('Delete a type')
    @api.response(201, 'Type successfully deleted.')
    def delete(self, type_id):
        return DBapi.types('DELETE', type_id)

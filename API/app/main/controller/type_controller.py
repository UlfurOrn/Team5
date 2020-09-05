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
        return DBapi.types('GET')

    @api.response(201, 'Type successfully created.')
    @api.doc('create a new Type')
    @api.expect(_type, validate=True)
    def post(self):
        data = request.json
        return DBapi.types('POST', data=data)


@api.route('/<type_id>')
@api.response(404, 'Type not found.')
class Type(Resource):
    @api.doc('Get a single type')
    def get(self, type_id):
        return DBapi.types('GET', type_id)

    @api.response(201, 'Type successfully updated.')
    @api.doc('Edit a type')
    def put(self, type_id):
        data = request.json
        return DBapi.types('PUT', type_id, data)

    @api.doc('Delete a type')
    @api.response(201, 'Type successfully deleted.')
    def delete(self, type_id):
        return DBapi.types('DELETE', type_id)

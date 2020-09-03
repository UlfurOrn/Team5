from flask import request
from flask_restplus import Resource
from ..services.dbapi import DBapi

from ..util.DTO.typeDTO import TypeDTO

api = TypeDTO.api

@api.route('/type')
class TypeList(Resource):
    @api.doc('List all types')
    def get(self):
        return DBapi.types('GET')

    @api.response(201, 'Type successfully created.')
    @api.doc('create a new Type')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return DBapi.types('POST',data=data)

@api.route('/type/<id>')
@api.response(404, 'Type not found.')
class Type(Resource):
    @api.doc('Get a single type')
    def get(self):
        return DBapi.('GET',id)

    @api.response(201, 'Type successfully updated.')
    @api.doc('Edit a type')
    def put(self):
        data = request.json
        return DBapi('PUT',id,data)

    @api.doc('Delete a type')
    @api.response(201, 'Type successfully deleted.')
    def delete(self):
        return DBapi('DELETE',id)
    
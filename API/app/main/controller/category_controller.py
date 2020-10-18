from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest, NotFound

from main.util.DTO.error_message import error_message
from main.util.mappers.categorymapper import CategoryMapper
from main.util.DTO.category_dto import CategoryDTO
from main.services.db_api import DBapi

api = CategoryDTO.api
_category = CategoryDTO.model


@api.route('')
class CategoryList(Resource):
    @api.doc('List all categories')
    @api.marshal_list_with(_category, envelope='categories')
    def get(self):
        data = DBapi.mcategories.get()

        category_list = []
        for category in data:
            category_list.append(category.to_dict())

        return category_list


@api.route('/<int:category_id>')
@api.response(400, 'BadRequest', error_message)
@api.response(404, 'Category not found.', error_message)
class SingleCategory(Resource):
    @api.doc('Get a single category')
    @api.marshal_with(_category)
    def get(self, category_id):
        check_id(category_id)

        data = DBapi.mcategories.get(category_id)
        category_dict = data[0].to_dict()
        return category_dict


def check_id(category_id):
    if category_id <= 0:
        raise BadRequest("Category id must be higher than 0")
    if not DBapi.mcategories.get(category_id):
        raise NotFound(f"Category with id {category_id} not found")

from flask import request
from flask_restplus import Resource

from main.util.mappers.categorymapper import CategoryMapper
from main.util.DTO.category_dto import CategoryDTO
from main.services.db_api import DBapi

api = McategoryDTO.api
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


@api.route('/<category_id>')
@api.response(404, 'Category not found.')
class SingleCategory(Resource):
    @api.doc('Get a single category')
    @api.marshal_with(_category)
    def get(self, category_id):
        data = DBapi.mcategories.get(category_id)
        if not data:
            return "", 404
        category_dict = data[0].to_dict()
        return category_dict

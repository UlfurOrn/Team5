from flask_restplus import Namespace, fields


class CategoryDTO:
    api = Namespace('category', description='Category related operations')
    model = api.model('Category', {
        "mcategoryid": fields.Integer(required=True, description='Category id'),
        "name": fields.String(required=True, description='Category name')
    })

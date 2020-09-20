from flask import request, jsonify
from flask_restplus import Resource, Namespace

api = Namespace('health', description='API health checker')

@api.route('')
class health(Resource):
    @api.doc('Get the health of the API')
    def get(self):
        resp = {'message': 'Healthy'}
        return jsonify(resp)
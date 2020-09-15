from flask import Flask
from flask_restplus import Api

from main.controller.record_controller import api as record_ns
from main.controller.type_controller import api as type_ns
from main.controller.user_controller import api as user_ns


app = Flask(__name__)
api = Api()

api.add_namespace(record_ns)
api.add_namespace(type_ns)
api.add_namespace(user_ns)

api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

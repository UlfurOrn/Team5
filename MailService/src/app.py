from flask import Flask
from flask_restplus import Api

from endpoints.subject import api as subject_ns
from endpoints.content import api as content_ns


app = Flask(__name__)
api = Api()

api.add_namespace(subject_ns)
api.add_namespace(content_ns)

api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8001)

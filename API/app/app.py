from flask import Flask
from main.util.api import api

from main.controller.record_controller import api as record_ns
from main.controller.habit_controller import api as habit_ns
from main.controller.user_controller import api as user_ns
from main.controller.health_controller import api as health_ns
from main.controller.auth_controller import api as auth_ns


app = Flask(__name__)
app.config['ERROR_404_HELP'] = False  # Remove extra message from 404 errors

api.add_namespace(record_ns)
api.add_namespace(habit_ns)
api.add_namespace(user_ns)
api.add_namespace(health_ns)
api.add_namespace(auth_ns)

api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

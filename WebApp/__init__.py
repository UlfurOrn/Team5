import os

from flask import Flask

def create_app():
    # Create and configure app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        API_URL = 'http://127.0.0.1:8000/',
        SECRET_KEY = 'dev',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .routes import auth
    app.register_blueprint(auth.bp)

    return app
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

    from .routes import auth, habits, account, index
    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(habits.bp)
    app.register_blueprint(account.bp)

    return app
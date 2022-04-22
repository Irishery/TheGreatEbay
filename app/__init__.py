import os
from flask import Flask
from flask_migrate import Migrate
from app.models import db, login_manager
import app.routes.routes_utils as route_utils

route_utils = route_utils

migrate = Migrate()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
upload_folder = os.environ.get('UPLOAD_FOLDER')

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.sign_in"
    login_manager.init_app(app)

    from .routes.main_route import main_route
    from .routes.auth import auth_route
    app.register_blueprint(main_route)
    app.register_blueprint(auth_route)

    from app.api.product_api import product_api
    app.register_blueprint(product_api)

    return app

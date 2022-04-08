from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    print(app.config)

    db.init_app(app)
    migrate.init_app(app)

    from .routes.main_route import main_route
    from .routes.auth import auth_route
    app.register_blueprint(main_route)
    app.register_blueprint(auth_route)

    return app

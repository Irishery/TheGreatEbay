from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    from .routes.main_route import main_route
    app.register_blueprint(main_route)

    return app

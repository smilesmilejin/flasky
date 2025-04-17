from flask import Flask
# from app.routes.hellow_world_routes import hello_world_bp
# from .routes.hello_world import hello_world_bp
from app.routes.cat_routes import cats_bp
def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)


    # app.register_blueprint(hello_world_bp)

    app.register_blueprint(cats_bp)

    return app
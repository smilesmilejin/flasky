from flask import Flask
from .db import db, migrate
from app.routes.cat_routes import cats_bp
from .models import cat
def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # connection string ends on database name
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'

    db.init_app(app) # Initialize a flask application with SQLALchemy extension created on line 7
    migrate.init_app(app, db) # Initialize the Migrate for handling database migrations

    app.register_blueprint(cats_bp)

    return app
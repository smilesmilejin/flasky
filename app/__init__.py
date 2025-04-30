from flask import Flask
from .db import db, migrate
from app.routes.cat_routes import cats_bp
from .models import cat
import os # os enables us to use environment variable

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # connection string ends on database name
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'
    
    # Use os.environ.get() to get the connection string from .env
    # os.environ is like a dictionary
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') 

    # This will switch to conftest.py Test Databse.
    if config:
        app.config.update(config)



    db.init_app(app) # Initialize a flask application with SQLALchemy extension created on line 7
    migrate.init_app(app, db) # Initialize the Migrate for handling database migrations

    app.register_blueprint(cats_bp)

    return app
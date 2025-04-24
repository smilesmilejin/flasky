## Added from 03 Building an API
# Create instance of SQLAlchemy and Migrate 

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models.base import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
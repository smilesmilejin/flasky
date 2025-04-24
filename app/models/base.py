# import the parent class DeclarativeBase, and
# create an empty subclass Base that we can give to our SQLAlchemy constructor.

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
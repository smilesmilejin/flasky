# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.personality = personality

# cats = [
#     Cat(1, "Luna", "grey", "naughty"),
#     Cat(2, "Morty", "orange", "orange"),
#     Cat(3, "Ash", "grey", "calm"),
#     Cat(4, "Luna", "brown", "cool"),
# ]


## Added from 03 Building an API
# do not forget the orm
from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

# Cat is the child class, inheritance from db. Model
class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped [str]
    personality: Mapped[str]
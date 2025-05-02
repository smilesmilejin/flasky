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

    # self for instance method
    # cls is for class method
    # I wrote this in my notes: Instance methods are called over instances of a class that already exist, 
    # and class methods are called over the class itself, 
    # for example, creating an instance that does not exist

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "personality": self.personality
        }
    
    # need this decorator to indicate this is a class method
    # common name for parameter in class method: cls
    @classmethod
    def from_dict(cls, cat_data):
        # cls refers to class name Cat
        # same as the following
        # new_cat = Cat(name = cat_data["name"],            
        #                color = cat_data["color"],
        #                 personality = cat_data["personality"])
        # return new_cat
        return cls(
            name = cat_data["name"],
            color = cat_data["color"],
            personality = cat_data["personality"]
        )
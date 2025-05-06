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
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import Optional
from sqlalchemy import ForeignKey

# Cat is the child class, inheritance from db. Model
class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped [str]
    personality: Mapped[str]
    # Added from 08 Building an API one-to-many relationship
    # table.column
    caretaker_id: Mapped[Optional[int]] = mapped_column(ForeignKey("caretaker.id"))
    # indicate relationship between caretaker and cat model
    # caretaker are associated with cats
    # back_populates: synchorize
    caretaker: Mapped[Optional["Caretaker"]] = relationship(back_populates="cats")
    
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
            "personality": self.personality,
            # termanry expression
            # None will converted into Null in json
            "caretaker": self.caretaker.name if self.caretaker_id else None
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
            name=cat_data["name"],
            color=cat_data["color"],
            personality=cat_data["personality"],
            # if there is not a key a caretaker_id int he cat_data, return None
            caretaker_id=cat_data.get("caretaker_id", None)
        )

#
# General Pattern
# class Parent(Base):
#     __tablename__ = "parent_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     children: Mapped[List["Child"]] = relationship(back_populates="parent")

# class Child(Base):
#     __tablename__ = "child_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
#     parent: Mapped["Parent"] = relationship(back_populates="children")
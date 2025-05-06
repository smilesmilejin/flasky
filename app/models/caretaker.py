from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

class Caretaker(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    # relationship with cat model, this model to synchorize with attribute called caretaker will out cat.
    # cats:This is the attribute name on the Caretaker model — 
    #     it will hold all the Cat instances associated with a particular caretaker.
    # Mapped[Optional[list["Cat"]]]: It will contain a list of Cat objects, because a caretaker can have many cats.
    
    # relationship(back_populates="caretaker")
    # This is a relationship, not a raw column (i.e., not a foreign key or scalar field).
    # It should look at the Cat model for a complementary relationship attribute 
    #     called "caretaker" (i.e., it assumes that in Cat, there’s a line like caretaker = relationship(back_populates="cats")).
    
    # Together, back_populates="caretaker" and back_populates="cats" define a bidirectional relationship, meaning:

    #     From a Cat instance, you can access .caretaker.
    #     From a Caretaker instance, you can access .cats.
    cats: Mapped[Optional[list["Cat"]]] = relationship(back_populates="caretaker")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, caretaker_data):
        new_caretaker = cls(name=caretaker_data["name"])
        return new_caretaker
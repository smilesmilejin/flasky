from flask import abort, Blueprint, make_response, request
from ..db import db
from app.models.cat import Cat

cats_bp = Blueprint("cats_bp", __name__, url_prefix = "/cats")

@cats_bp.post("")
def create_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    personality = request_body["personality"]

    new_cat = Cat(name=name, color=color, personality=personality)
    db.session.add(new_cat)
    db.session.commit()

    response = {
    	"id": new_cat.id,
        "name": new_cat.name,
        "color": new_cat.color,
        "personality": new_cat.personality
    }

    return response, 201

@cats_bp.get("")
def get_all_cats():
    query = db.select(Cat).order_by(Cat.id)
    cats = db.session.scalars(query)

    cats_response = []
    for cat in cats: 
        cats_response.append(
            {
                "id": cat.id,
                "name": cat.name,
                "color": cat.color,
                "personality": cat.personality
            }
        )

    return cats_response

def validate_cat(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Cat id ({id}) is invalid."}
        abort(make_response(invalid, 400))

    for cat in cats:
        if cat.id == id:
            return cat 
    
    not_found = {"message": f"Cat with id ({id}) not found."}
    abort(make_response(not_found, 404))



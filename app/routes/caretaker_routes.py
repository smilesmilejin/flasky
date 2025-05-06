from flask import abort, Blueprint, make_response, request
from app.models.caretaker import Caretaker
from app.models.cat import Cat
from .route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db

bp = Blueprint("caretakers_bp", __name__, url_prefix="/caretakers")

@bp.post("")
def create_caretaker():
    request_body = request.get_json()

    return create_model(Caretaker, request_body)

@bp.post("/<id>/cats")
def create_cat_with_caretaker_id(id):
    caretaker = validate_model(Caretaker, id)
    request_body = request.get_json()
    request_body["caretaker_id"] = caretaker.id

    return create_model(Cat, request_body)

@bp.get("")
def get_all_caretakers():
    return get_models_with_filters(Caretaker, request.args)

@bp.get("/<id>/cats")
def get_all_caretaker_cats(id):
    caretaker = validate_model(Caretaker, id)
    cats = [cat.to_dict() for cat in caretaker.cats]

    print(caretaker.cats)

    return cats

from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.cat import Cat
from app.models.caretaker import Caretaker
from .route_utilities import validate_model, create_model, get_models_with_filters

# blueprint is usually bp, when import give it an alis
bp = Blueprint("caretakers_bp", __name__, url_prefix = "/caretakers")



@bp.post("")
def create_caretaker():
    request_body = request.get_json()
    return create_model(Caretaker, request_body)

    # try:
    #     new_caretaker = Caretaker.from_dict(request_body)
    # except KeyError as e:
    #     response = {"message": f"Invalid request: missing {e.args[0]}"}
    #     abort(make_response(response, 400))

    # db.session.add(new_caretaker)
    # db.session.commit()

    # return new_caretaker.to_dict(), 201


# id is the caretaker id
@bp.post("/<id>/cats")
def create_cat_with_caretaker_id(id):
    caretaker = validate_model(Caretaker, id)
    request_body = request.get_json()

    request_body["caretaker_id"] = caretaker.id

    return create_model(Cat, request_body)

    # try:
    #     new_cat = Cat.from_dict(request_body)
    # except KeyError as e:
    #     response = {"message": f"Invalid request: missing {e.args[0]}"}
    #     abort(make_response(response, 400))

    # db.session.add(new_cat)
    # db.session.commit()

    # return new_cat.to_dict(), 201



@bp.get("")
def get_all_caretakers():
    return get_models_with_filters(Caretaker, request.args)

    # query = db.select(Caretaker)

    # name_param = request.args.get("name")
    # if name_param:
    #     query = query.where(Caretaker.name == name_param)

    # caretakers = db.session.scalars(query)

    # caretakers_response = []
    # for caretaker in caretakers:
    #     caretakers_response.append(caretaker.to_dict())

    # return caretakers_response


@bp.get("/<id>/cats")
def get_all_caretaker_cats(id):
    caretaker = validate_model(Caretaker, id)
    cats = [cat.to_dict() for cat in caretaker.cats]

    # this will be a list of cat object
    # print(caretaker.cats)
    return cats
from flask import Blueprint, abort, make_response
# from app.models.cat import cats
from ..models.cat import cats

import json

cats_bp = Blueprint("cat_bp", __name__, url_prefix = "/cats")

# Decorator question
# @cats_bp.get("")
# It is the same as : @cats_bp.get("", strict_slashes=False)

# Single forward / is the default
# @cats_bp.get(“”) and @cats_bp.get(“/“): the same route
    # Always use "/" for the root path of a router.?

# Some frameworks normalize trailing slashes. 
# FastAPI and Flask can treat /cats and /cats/ the same depending on how you configure them.
# If you're strict about trailing slashes (strict_slashes=True in Flask), then /cats and /cats/ could be treated differently.

@cats_bp.get("")                                 
def get_all_cats():

    results_list = []

    for cat in cats:
        results_list.append(dict(
            id = cat.id,
            name = cat.name,
            color = cat.color,
            personality = cat.personality)
        )


    return results_list

    #The previous results_list sort the key alphabetically,
    # Method 2:  To make the id appears first
    # cats_list = []
    # for cat in cats:
    #     this_cat = {
    #         "id": cat.id,
    #         "name":cat.name,
    #         "color": cat.color,
    #         "personality": cat.personality
    #     }
    #     cats_list.append(this_cat)
    
    # return json.dumps(cats_list, indent=2, sort_keys=False)

# <id> is the route parameter
# like a placeholder for cat id
        # /cats/1
# /<id> must match the parameter of get_one_cat(id)
@cats_bp.get("/<id>")
def get_one_cat(id):
    # pass
    #print(type(id)) # <class 'str'>
    cat = validate_cat(id)


    cat_dict ={
        "id": cat.id,
        "name":cat.name,
        "color": cat.color,
        "personality": cat.personality
    }
    return cat_dict


def validate_cat(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {'message': f"Cat id ({id}) is invalid."}
        # 400 bad request
        abort(make_response(invalid, 400))

    for cat in cats:
        if cat.id == id:
            return cat
    
    not_found = {'message': f"Cat with id ({id}) not found"}
    abort(make_response(not_found, 404))
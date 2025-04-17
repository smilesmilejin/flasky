from flask import Blueprint

# from app.models.cat import cats
from ..models.cat import cats

import json

cats_bp = Blueprint("cat_bp", __name__, url_prefix = "/cats")

@cats_bp.get("/")
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

@cats_bp.get("/<id>")
def get_one_cat():
    pass

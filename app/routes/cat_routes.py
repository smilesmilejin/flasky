# from flask import Blueprint, abort, make_response
# # from app.models.cat import cats
# # from ..models.cat import cats

# import json

# cats_bp = Blueprint("cat_bp", __name__, url_prefix = "/cats")

# # Decorator question
# # @cats_bp.get("")
# # It is the same as : @cats_bp.get("", strict_slashes=False)

# # Single forward / is the default
# # @cats_bp.get(“”) and @cats_bp.get(“/“): the same route
#     # Always use "/" for the root path of a router.?

# # Some frameworks normalize trailing slashes. 
# # FastAPI and Flask can treat /cats and /cats/ the same depending on how you configure them.
# # If you're strict about trailing slashes (strict_slashes=True in Flask), then /cats and /cats/ could be treated differently.

# @cats_bp.get("")                                 
# def get_all_cats():

#     results_list = []

#     for cat in cats:
#         results_list.append(dict(
#             id = cat.id,
#             name = cat.name,
#             color = cat.color,
#             personality = cat.personality)
#         )


#     return results_list

#     #The previous results_list sort the key alphabetically,
#     # Method 2:  To make the id appears first
#     # cats_list = []
#     # for cat in cats:
#     #     this_cat = {
#     #         "id": cat.id,
#     #         "name":cat.name,
#     #         "color": cat.color,
#     #         "personality": cat.personality
#     #     }
#     #     cats_list.append(this_cat)
    
#     # return json.dumps(cats_list, indent=2, sort_keys=False)

# # <id> is the route parameter
# # like a placeholder for cat id
#         # /cats/1
# # /<id> must match the parameter of get_one_cat(id)
# @cats_bp.get("/<id>")
# def get_one_cat(id):
#     # pass
#     #print(type(id)) # <class 'str'>
#     cat = validate_cat(id)


#     cat_dict ={
#         "id": cat.id,
#         "name":cat.name,
#         "color": cat.color,
#         "personality": cat.personality
#     }
#     return cat_dict


# def validate_cat(id):
#     try:
#         id = int(id)
#     except ValueError:
#         invalid = {'message': f"Cat id ({id}) is invalid."}
#         # 400 bad request
#         abort(make_response(invalid, 400))

#     for cat in cats:
#         if cat.id == id:
#             return cat
    
#     not_found = {'message': f"Cat with id ({id}) not found"}
#     abort(make_response(not_found, 404))

######### Added from 03 Building an API

from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.cat import Cat
from .route_utilities import validate_model, create_model, get_models_with_filters

# blueprint is usually bp, when import give it an alis
bp = Blueprint("cat_bp", __name__, url_prefix = "/cats")

@bp.post("")
def create_cat():

    request_body = request.get_json()
    return create_model(Cat, request_body)

    # request_body = request.get_json()


    # # name = request_body["name"]
    # # color = request_body["color"]
    # # personality = request_body["personality"]
    # # new_cat = Cat(name=name, color=color, personality=personality)

    # new_cat= Cat.from_dict(request_body)
    # db.session.add(new_cat)
    # db.session.commit()

    # # response = {
    # #     "id": new_cat.id,
    # #     "name": new_cat.name,
    # #     "color": new_cat.color,
    # #     "personality": new_cat.personality
    # # }

    # # Use instance method to dict() to create a dictionary
    # return new_cat.to_dict(), 201

@bp.get("")
def get_all_cats():
    # Added from 07 Building an API one to many
    return get_models_with_filters(Cat, request.args)

    # ######### Added from 05 Building an API Livecode Query Params
    # query = db.select(Cat)
    
    # name_param = request.args.get("name")
    # if name_param:
    #     query = query.where(Cat.name == name_param)
    
    # color_param = request.args.get("color")
    # if color_param:
    #     query = query.where(Cat.color.ilike(f"%{color_param}"))

    # # query = query.orderby(Cat.id.desc)
    # # query = query.order_by(Cat.id)
    # query = query.order_by(Cat.name.desc())


    # ######### End from 05 Building an API Livecode Query Params

    # # query = db.select(Cat).order_by(Cat.id)
    # cats = db.session.scalars(query)

    # cats_response = []
    # for cat in cats:
    #     cats_response.append(cat.to_dict()
    #     )
    # return cats_response

######### Added from 04 Building an API Livecode -Read, Update and Delete

@bp.get("/<id>")
def get_one_cat(id):
    # we changes validate_model(cls, model_id)
    cat = validate_model(Cat, id)
    # cat = validate_cat(id)

    return cat.to_dict()

# Update record
@bp.put("/<id>")
def update_cat(id):
    # cat = validate_cat(id)
    cat = validate_model(Cat, id)

    # Get information from request body
    request_body = request.get_json()
    
    # Update database
    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.personality = request_body["personality"]

    db.session.commit()

    # mimetype default is html
    return Response(status=204, mimetype='application/json')

# Delte record
@bp.delete("/<id>")
def delete_cat(id):
    cat = validate_model(Cat, id)
    # cat = validate_cat(id)

    db.session.delete(cat)
    db.session.commit()

    # mimetype default is html
    return Response(status=204, mimetype='application/json')



# def validate_cat(id):
#     try:
#         id = int(id)
#     except ValueError:
#         invalid = {'message': f"Cat id ({id}) is invalid."}
#         # 400 bad request
#         abort(make_response(invalid, 400))

#     query = db.select(Cat).where(Cat.id == id)
#     # use scalar to singular
#     # SQLAlchemry will return None if not found
#     cat = db.session.scalar(query)

#     if not cat:
#         not_found = {'message': f"Cat with id ({id}) not found"}
#         abort(make_response(not_found, 404))
    
#     return cat

# Move this to another file
# def validate_model(cls, model_id):
#     try:
#         id = int(model_id)
#     except ValueError:
#         invalid = {'message': f"{cls.__name__} id ({model_id}) is invalid."}
#         # 400 bad request
#         abort(make_response(invalid, 400))

#     # change Cat to cls
#     query = db.select(cls).where(cls.id == model_id)
#     # use scalar to singular
#     # SQLAlchemry will return None if not found
#     model = db.session.scalar(query)

#     if not model:
#         not_found = {'message': f"{cls.__name__} with id ({model_id}) not found"}
#         abort(make_response(not_found, 404))
    
#     return model
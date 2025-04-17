from flask import Blueprint

hello_world_bp = Blueprint("hello_world_bp", __name__)


# Single forward / is the default
@hello_world_bp.get("/")
def say_hello_world():
    return "Hello, world!"
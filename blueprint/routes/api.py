from urllib import request

from flask import Blueprint

from ..methods import display, display_id, add_course, modify, delete

from ..models.course import Course
from ..certAuth.auth import certAuth

api = Blueprint('api', __name__)


@api.route("/", methods=['GET'])
@certAuth
def home():
    return "<h1>Welcome to Course API</h1>", 200


# FETCH ALL THE COURSES IN A LIST
@api.route("/courses", methods=['GET'])
@certAuth
def get_courses():
    return display()


# FETCH THE COURSE BASED ON ID
@api.route("/courses/<int:id>", methods=["GET"])
@certAuth
def get_course(id):
    cour = Course.query.get(id)
    return display_id(id)


# CREATE NEW COURSES AND COMMITTING TO DATABASE POST REQ
@api.route("/append", methods=["POST"])
@certAuth
def create_course():
    return add_course()


# updating the data
@api.route("/courses/<int:id>", methods=["PUT"])
@certAuth
def update_course(id):
    if not request.json:
        return "Invalid_json_data"
    return modify(id)


# DELETE THE COURSE ITEMS
@api.route("/courses/<int:id>", methods=["DELETE"])
@certAuth
def delete_course(id):
    return delete(id)

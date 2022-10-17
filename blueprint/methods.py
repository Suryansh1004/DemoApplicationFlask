from flask import request, jsonify
from blueprint import custom_logger
from .models.course import Course
from .extensions import db

# initializing custom_logger module
log = custom_logger.logg(__name__)
log.info("Start Application")


def display():
    cour = Course.query.all()
    log.info("Displaying all the courses")
    return jsonify([itr.to_json() for itr in cour])


# get course using id
def display_id(id):
    cour = Course.query.get(id)
    if cour is None:
        log.info("Course  Doesn't Exists")
        return jsonify({"Course  Doesn't Exists": True})
    log.info("Course by ID")
    return jsonify(cour.to_json())


# create course
def add_course():
    if not request.json:
        log.info("Invalid Json Data")
        return jsonify({"Invalid Data": True})
    cour = Course(
        name=request.json.get('name'),
        description=request.json.get('description'),
        duration=request.json.get('duration')
    )
    db.session.add(cour)
    db.session.commit()
    log.info("Adding Course")
    return jsonify(cour.to_json())


# PUT request
def modify(id):
    cour = Course.query.get(id)
    if cour is None:
        log.info("Course Doesn't exist")
        return jsonify({"Course  Doesn't Exists": True})
    cour.name = request.json.get('name', cour.name)
    cour.description = request.json.get('description', cour.description)
    cour.duration = request.json.get('duration', cour.duration)
    db.session.commit()
    log.info("Modified course data")
    return jsonify(cour.to_json())


# deleting data
def delete(id):
    cour = Course.query.get(id)
    if cour is None:
        log.info("Invalid Course Id")
        return "Course  Doesn't Exists"
    log.info("Deleting Course")
    db.session.delete(cour)
    db.session.commit()
    # [itr.to_json() for itr in cour]
    return jsonify({'Deleted': True})

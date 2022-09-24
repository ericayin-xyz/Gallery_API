from unittest import result
from flask import Blueprint, jsonify, request 
from main import db
from models.visitors import Visitor
from schemas.visitor_schema import visitor_schema, visitors_schema

visitors = Blueprint('visitors', __name__, url_prefix="/visitors")

# The GET routes endpoint
@visitors.route("/", methods=["GET"])
def get_visitors():
    visitors_list = Visitor.query.all()
    result = visitors_schema.dump(visitors_list)
    return jsonify(result)

@visitors.route("/<int:id>", methods=["GET"])
def get_visitor(id):
    visitor = Visitor.query.get(id)
    if not visitor:
        return {"error": "Visitor id not found"}
    result = visitor_schema.dump(visitor)
    return jsonify(result)

# POST routes endpoint
@visitors.route("/", methods=["POST"])
def create_visitor():
    # get the values from the request and load them with the single schema
    visitor_fields = visitor_schema.load(request.json)
    # create a new visitor object
    visitor = Visitor(
        username = visitor_fields["user_name"],
        email = visitor_fields["email"],
        password = visitor_fields["password"],
    )

    db.session.add(visitor)
    # store in the database and save the changes
    db.session.commit()

    return jsonify(visitor_schema.dump(visitor))

# DELETE routes endpoint
@visitors.route("/<int:id>", methods=["DELETE"])
def delete_visitor(id):
    visitor = Visitor.query.get(id)
    if not visitor:
        return {"error": "Visitor id not found"}

    db.session.delete(visitor)
    db.session.commit()

    # return jsonify(visitor_schema.dump(visitor))
    return {"message": "Visitor removed successfully"}
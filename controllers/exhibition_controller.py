from flask import Blueprint, jsonify, request 
from main import db
from models.exhibition import Exhibition
from models.gallery import Gallery
from schemas.exhibition_schema import exhibition_schema, exhibitions_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

exhibitions = Blueprint('exhibitions', __name__, url_prefix="/exhibitions")

# The GET routes endpoint
@exhibitions.route("/", methods=["GET"])
def get_exhibitions():
    exhibitions_list = Exhibition.query.all()
    result = exhibitions_schema.dump(exhibitions_list)
    return jsonify(result)

@exhibitions.route("/<int:id>", methods=["GET"])
def get_exhibition(id):
    exhibition = Exhibition.query.filter_by(exhibition_id=id).first()
    if not exhibition:
        return {"error": "Exhibition not found"}
    return jsonify(exhibition_schema.dump(exhibition))


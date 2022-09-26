from flask import Blueprint, jsonify, request 
from main import db
from models.gallerys import Gallery
from schemas.gallery_schema import gallery_schema, gallerys_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

exhibitions = Blueprint('exhibitions', __name__, url_prefix="/exhibitions")

# The GET routes endpoint
@exhibitions.route("/", methods=["GET"])
def get_exhibitions():
    exhibitions_list = Gallery.query.all()
    result = gallerys_schema.dump(exhibitions_list)
    return jsonify(result)

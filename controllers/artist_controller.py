from flask import Blueprint, jsonify, request 
from main import db
from models.artist import Artist
from models.gallerys import Gallery
from schemas.gallery_schema import gallery_schema, gallerys_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

artists = Blueprint('artists', __name__, url_prefix="/artists")

# The GET routes endpoint
@artists.route("/", methods=["GET"])
def get_artists():
    artists_list = Artist.query.all()
    result = gallerys_schema.dump(artists_list)
    return jsonify(result)

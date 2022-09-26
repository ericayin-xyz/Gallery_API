from flask import Blueprint, jsonify, request 
from main import db
from models.artwork import Artwork
from schemas.artwork_schema import artwork_schema, artworks_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

artworks = Blueprint('artworks', __name__, url_prefix="/artworks")

# The GET routes endpoint
@artworks.route("/", methods=["GET"])
def get_artworks():
    artworks_list = Artwork.query.all()
    result = artworks_schema.dump(artworks_list)
    return jsonify(result)

@artworks.route("/<int:id>", methods=["GET"])
def get_artwork(id):
    # artwork = Artworks.query.get(id)
    artwork = Artwork.query.filter_by(artwork_id=id).first()
    # check if  we found artworks
    if not artwork:
        return {"error": "Artworks not found"}
    return jsonify(artwork_schema.dump(artwork))

# The POST routes endpoint
@artworks.route("/", methods=["POST"])
# @jwt_required()
def new_artwork():
    # if get_jwt_identity() != "admin":
    #     return {"error": "You don't have the permission to do this"}
    artwork_fields = artwork_schema.load(request.json)
    artwork = Artwork(
        title = artwork_fields["title"],
        publish_date = artwork_fields["publish_date"],
        start_date = artwork_fields["start_date"],
        end_date = artwork_fields["end_date"],
        description = artwork_fields["description"],
        artwork_type = artwork_fields["artwork_type"],
        artwork_url = artwork_fields["artwork_url"],
        artist_id = artwork_fields["artist_id"]
    )

    db.session.add(artwork)
    db.session.commit()
    return jsonify(artwork_schema.dump(artwork)), 201

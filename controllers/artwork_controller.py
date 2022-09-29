from flask import Blueprint, jsonify, request 
from main import db
from models.artwork import Artwork
from schemas.artwork_schema import artwork_schema, artworks_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date

artworks = Blueprint('artworks', __name__, url_prefix="/artworks")

@artworks.route("/", methods=["GET"])
def get_artworks():
    artworks_list = Artwork.query.all()
    result = artworks_schema.dump(artworks_list)
    return jsonify(result)

@artworks.route("/<int:id>/", methods=["GET"])
def get_artwork(id):
    artwork = Artwork.query.get(id)
    artwork = Artwork.query.filter_by(artwork_id=id).first()
    # check if  we found artworks
    if not artwork:
        return {"error": "Artwork not found"}
    return jsonify(artwork_schema.dump(artwork))

@artworks.route("/", methods=["POST"])
# @jwt_required()
def new_artwork():
    # it is not enough with a token, the identity needs to be admin
#     if get_jwt_identity() != "admin":
#         return {"error": "You don't have the permission to do this"}

    artwork_fields = artwork_schema.load(request.json)
    new_artwork = Artwork(
        title = artwork_fields["title"],
        publish_date = artwork_fields["publish_date"],
        description = artwork_fields["description"],
        artwork_type = artwork_fields["artwork_type"],
        artwork_url = artwork_fields["artwork_url"],
        artist_id = artwork_fields["artist_id"]
    )
    db.session.add(new_artwork)
    db.session.commit()
    return jsonify(artwork_schema.dump(new_artwork))

@artworks.route("/<int:id>/", methods=["PUT"])
# @jwt_required()
def update_gallery(id):
    # if get_jwt_identity() != "admin":
    #     return {"error": "You don't have the permission to do this"}
    artwork = Artwork.query.get(id)
    if not artwork:
        return {"error": "Artwork not found"}
    artwork_fields = artwork_schema.load(request.json)

    artwork.title = artwork_fields["title"],
    artwork.publish_date = artwork_fields["publish_date"],
    artwork.artist_id = artwork_fields["artist_id"],
    artwork.description = artwork_fields["description"],
    artwork.artwork_url = artwork_fields["artwork_url"],
    artwork.artwork_type = artwork_fields["artwork_type"]

    db.session.commit()
    return jsonify( artwork_schema.dump( artwork))

@artworks.route("/<int:id>/", methods=["DELETE"])
# @jwt_required()
def delete_gallery(id):
    # if get_jwt_identity() != "admin":
    #     return {"error": "You don't have the permission to do this"}
    artwork = Artwork.query.filter_by(id=id).first()
    if not artwork:
        return {"error": "Artwork not found"}
    
    db.session.delete(artwork)
    db.session.commit()
    return jsonify(artwork_schema.dump(artwork))
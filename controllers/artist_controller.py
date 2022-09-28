from flask import Blueprint, jsonify, request 
from main import db
from models.artist import Artist
from schemas.artist_schema import artists_schema, artist_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


artists = Blueprint('artists', __name__, url_prefix="/artists")

# The GET routes endpoint
@artists.route("/", methods=["GET"])
def get_artists():
    artists_list = Artist.query.all()
    result = artists_schema.dump(artists_list)
    return jsonify(result)

@artists.route("/<int:id>", methods=["GET"])
def get_artist(id):
    artist = Artist.query.get(id)
    if not artist:
        return {"error": "Artists not found"}
    return jsonify(artist_schema.dump(artist))

# The POST routes endpoint
@artists.route("/", methods=["POST"])
@jwt_required()
def add_artist():
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}

    artist_fields = artist_schema.load(request.json)
    new_artist = Artist(
        name = artist_fields["name"],
        dob = artist_fields["dob"],
        biography = artist_fields["biography"]
    )
    db.session.add(new_artist)
    db.session.commit()
    return jsonify(artist_schema.dump(new_artist)), 201

@artists.route("/<int:id>/", methods=["DELETE"])
# @jwt_required()
def delete_artist(id):
    # if get_jwt_identity() != "admin":
    #     return {"error": "You don't have the permission to do this"}

    artist = Artist.query.filter_by(id=id).first()
    if not artist:
        return {"error": "Artist does not exist"}       
    db.session.delete(artist)
    db.session.commit()
    return jsonify(artist_schema.dump(artist))
    
@artists.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_gallery(id):
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}

    artist = Artist.query.get(id)
    if not artist:
        return {"error": "Artist not found in the database"}
    artist_fields = artist_schema.load(request.json)

    artist.name = artist_fields["name"],
    artist.dob = artist_fields["dob"], 
    artist.biography = artist_fields["biography"]

    db.session.commit()
    return jsonify(artist_schema.dump(artist))

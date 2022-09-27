from flask import Blueprint, jsonify, request 
from main import db
from models.artist import Artist
from models.gallery import Gallery
from schemas.artist_schema import artists_schema, artist_schema
from datetime import date
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







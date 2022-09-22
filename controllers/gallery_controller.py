from flask import Blueprint, jsonify, request 
from app import db 
from models.Gallery import Gallery

gallery = Blueprint('gallery', __name__, url_prefix="/gallery")

# The GET routes endpoint
@gallery.route('/', methods=["GET"])
def get_gallery():
    # get all gallerys from the database table
    gallery_list = Gallery.query.all()
    # Convert the gallerys from the database into a JSON format and store them in result
    result = gallery_schema.dump(gallery_list)
    # return the data in JSON format
    return "List of gallerys retrieved"

# The POST route endpoint
@gallery.route('/', methods=["POST"])
def creat_gallery():
    # add a new gallery
    return "Gallery created"

# round out our CRUD resource with a DELETE method
@gallery.route("/<int:id>/", methods=["DELETE"])
def delete_gallery(id):
    return "Gallery deleted"
    
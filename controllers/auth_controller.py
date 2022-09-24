from base64 import decode
from datetime import timedelta
from os import abort
from flask import Blueprint, jsonify, request
from main import db, bcrypt, jwt
from flask_jwt_extended import create_access_token
from models.admin import Admin
from schemas.admin_schema import admin_schema

auth = Blueprint('admin', __name__, url_prefix="/auth")

@auth.route("/register", methods=["post"])
def register_admin():
    # get the admin details from the request
    admin_fields = admin_schema.load(request.json)

    # find admin by username to check if they are already in the database
    admin = Admin.query.filter_by(username=admin_fields["username"]).first()
    if admin:
        return {"error": "Name already registered"}
    # find admin by email to check if they are already in the database
    admin = Admin.query.filter_by(email=admin_fields["email"]).first()
    if admin:
        return {"error": "Email already registered"}

    # create a new admin object
    admin = Admin(
        username = admin_fields["username"],
        email = admin_fields["email"],
        password = bcrypt.generate_password_hash(admin_fields["password"]).decode("utf8")
    )

    # add the admin and save changes to the database
    db.session.add(admin)
    db.session.commit()

    # generate the token setting the identity (admin.id) and expiry time (30 minutes)
    token = create_access_token(identity=str(admin.admin_id), expires_delta=timedelta(minutes=30))
    
    return {"username": admin.username, "token": token}
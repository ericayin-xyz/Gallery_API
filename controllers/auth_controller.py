from datetime import timedelta
from os import abort
from xml.dom import ValidationErr
from flask import Blueprint, jsonify, request
from main import db, bcrypt, jwt
from flask_jwt_extended import create_access_token
from models.admin import Admin
from models.visitors import Visitor
from schemas.admin_schema import admin_schema
from schemas.visitors_schema import visitor_schema
from marshmallow.exceptions import ValidationError

auth = Blueprint('auth', __name__, url_prefix="/auth")


@auth.route("/register", methods=["POST"])
def register_visitors():
    # get the visitor details from the request
    visitor_fields = visitor_schema.load(request.json)

    # find the visitor by username to check if they are registered
    visitor = Visitor.query.filter_by(username=visitor_fields["username"]).first()
    if visitor:
        return {"error": "Usename already registered"}

    # find visitor by email to check if they are registered
    visitor = Visitor.query.filter_by(email=visitor_fields["email"]).first()
    if visitor:
        return {"error": "Email already registered"}

    # create visitor object
    visitor = Visitor(
        username = visitor_fields["username"],
        email = visitor_fields["email"],
        password = bcrypt.generate_password_hash(visitor_fields["password"]).decode("utf8")
    )
    # add the visitor to the database
    db.session.add(visitor)
    db.session.commit()

    # generate the token setting the identity&expiry time
    token = create_access_token(identity=str(visitor.visitor_id), expires_delta=timedelta(minutes=30))
    return {"username": visitor.username, "token": token}


# @auth.route("/register", methods=["POST"])
# def register_auth():
#     # get the admin details from the request
#     admin_fields = admin_schema.load(request.json)

#     # find admin by username to check if they are already in the database
#     admin = Admin.query.filter_by(username=admin_fields["username"]).first()
#     if admin:
#         return {"error": "Username already registered"}

#     # find admin by email to check if they are already in the database
#     admin = Admin.query.filter_by(email=admin_fields["email"]).first()
#     if admin:
#         return {"error": "Email already registered"}

#     # create a new admin object
#     admin = Admin(
#         username = admin_fields["username"],
#         full_name = admin_fields["full_name"],
#         email = admin_fields["email"],
#         shift = admin_fields["shift"],
#         password = bcrypt.generate_password_hash(admin_fields["password"]).decode("utf8")
#     )

#     # add the admin and save changes to the database
#     db.session.add(admin)
#     db.session.commit()

#     # generate the token setting the identity (admin.id) and expiry time (30 minutes)
#     token = create_access_token(identity=str(admin.admin_id), expires_delta=timedelta(minutes=30))
#     return {"username": admin.username, "token": token}

# login visitors POST
@auth.route("/login", methods=["POST"])
def login_visitors():
    # get username and password from the request
    visitor_fields = visitor_schema.load(request.json)
    # check username and password, user needs to exist, and password needs to match
    visitor = Visitor.query.filter_by(username=visitor_fields["username"]).first()
    if not visitor:
        return {"error": "Username is not valid"}
    if not bcrypt.check_password_hash(visitor.password, visitor_fields["password"]):
        return {"error": "wrong password"}

    #credentials are vialid, so generate token and return it to the user   
    token = create_access_token(identity=str(visitor.visitor_id), expires_delta=timedelta(minutes=30))

    return {"username": visitor.username, "token": token}

# login admin POST
@auth.route("/admin/login", methods=["POST"])
def login_admin():
    # get username and password from the request
    admin_fields = admin_schema.load(request.json)
    # check username and password, user needs to exist, and password needs to match
    admin = Admin.query.filter_by(username=admin_fields["username"]).first()
    if not admin:
        return {"error": "Username is not valid"}
    if not bcrypt.check_password_hash(admin.password, admin_fields["password"]):
        return {"error": "wrong password"}

    #credentials are vialid, so generate token and return it to the user   
    token = create_access_token(identity="admin", expires_delta=timedelta(minutes=30))

    return {"admin": admin.username, "token": token}

@auth.errorhandler(ValidationError)
def register_validation_error(error):
    # print(errror.messages)
    return error.messages, 400



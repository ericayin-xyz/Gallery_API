from flask import Blueprint, jsonify, request 
from main import db
from models.exhibition import Exhibition
from models.ticket import Ticket
from models.visitor import Visitor
from schemas.exhibition_schema import exhibition_schema, exhibitions_schema
from schemas.ticket_schema import ticket_schema, tickets_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date, datetime

exhibitions = Blueprint('exhibitions', __name__, url_prefix="/exhibitions")

# The GET routes endpoint
@exhibitions.route("/", methods=["GET"])
def get_exhibitions():
    exhibitions_list = Exhibition.query.all()
    result = exhibitions_schema.dump(exhibitions_list)
    return jsonify(result)

@exhibitions.route("/<int:id>/", methods=["GET"])
def get_exhibition(id):
    exhibition = Exhibition.query.filter_by(exhibition_id=id).first()
    if not exhibition:
        return {"error": "Exhibition not found"}
    return jsonify(exhibition_schema.dump(exhibition))

@exhibitions.route("/tickets/", methods=["GET"])
@jwt_required()
def get_all_tickets():
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}
    tickets_list = Ticket.query.all()
    return jsonify(tickets_schema.dump(tickets_list))


# The POST routes endpoint
# admin adds new exhibitions
@exhibitions.route("/", methods=["POST"])
@jwt_required()
def new_exhibition():
    # if get_jwt_identity != "admin":
    #     return {"error": "You don't have the permission to do this"}
    exhibition_fields = exhibition_schema.load(request.json)
    new_exhibition = Exhibition(
        name = exhibition_fields["name"],
        start_date = exhibition_fields["start_date"],
        end_date = exhibition_fields["end_date"],
        artwork_id = exhibition_fields["artwork_id"]
    )
    db.session.add(new_exhibition)
    db.session.commit()
    return jsonify(exhibition_schema.dump(new_exhibition))

# visitor posts a new ticket
@exhibitions.route("<int:exhibition_id>/tickets", methods=["POST"])
@jwt_required()
def new_ticket(exhibition_id):
    exhibition = Exhibition.query.get(exhibition_id)
    if not exhibition:
        return {"error": "Exhibition not found"}
    visitor_id = get_jwt_identity()
    visitor = Visitor.query.get(visitor_id)
    if not visitor:
        return {"error": "Visitor not found"}

    ticket = Ticket(
        visitor = visitor,
        exhibition = exhibition,
        gallery_id = get_jwt_identity(),
        entry_date = date.today(),
        entry_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )

    db.session.add(ticket)
    db.session.commit()

    return jsonify(ticket_schema.dump(ticket))




    # if get_jwt_identity != "admin":
    #     return {"error": "You don't have the permission to do this"}
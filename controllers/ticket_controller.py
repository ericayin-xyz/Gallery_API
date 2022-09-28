from flask import Blueprint, jsonify, request 
from main import db
from models.ticket import Ticket
from schemas.ticket_schema import ticket_schema, tickets_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

tickets = Blueprint('tickets', __name__, url_prefix="/tickets")

@tickets.route("/", methods=["GET"])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify(tickets_schema.dump(tickets))

@tickets.route("/<int:id>/", methods=["GET"])
def get_ticket(id):
    ticket = Ticket.query.get(id)
    if not ticket:
        return {"error": "Ticket not found"}
    return jsonify(ticket_schema.dump(ticket))

@tickets.route("/<int:id>/", methods=["PUT"])
# @jwt_required()
def update_ticket(id):
    # if get_jwt_identity() != "admin":
    #     return {"error": "You don't have the permission to do this"}
    ticket = Ticket.query.get(id)
    # check if the ticket exists in the database
    if not ticket:
        return {"error": "Ticket not found in the database"}
    # get the ticket from the request
    ticket_fields = ticket_schema.load(request.json)

    # modify the ticket
    ticket.entry_date = ticket_fields["entry_date"],
    ticket.entry_time = ticket_fields["entry_time"],
    ticket.purchasing_time = ticket_fields["purchasing_time"],
    ticket.gallery_id = ticket_fields["gallery_id"],
    ticket.exhibition_id = ticket_fields["exhibition_id"]

    # save changes to the database
    db.session.commit()
    return jsonify(ticket_schema.dump(ticket))

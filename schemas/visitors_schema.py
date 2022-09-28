from main import ma
from marshmallow.validate import Length
from marshmallow import fields
from schemas.ticket_schema import TicketSchema

class VisitorSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["visitor_id", "username", "email", "password"]
        # load_only = ['artist_id']
    
    # add validation to password
    password = ma.String(validate=Length(min=6))
    username = ma.String(required = True)

visitor_schema = VisitorSchema()



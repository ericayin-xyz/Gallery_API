from main import ma
from marshmallow.validate import Length

class VisitorSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["visitor_id", "username", "email", "password"]
    # add validation to password
    password = ma.String(validate=Length(min=6, max=13))
    username = ma.String(required = True)

visitor_schema = VisitorSchema()
visitors_schema = VisitorSchema(many=True)





from wsgiref import validate
from main import ma
from marshmallow.validate import Length

class VisitorSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["visitor_id", "full_name", "email", "password"]
    # add validation to password
    password = ma.String(validate=Length(min=6, max=13))


visitor_schema = VisitorSchema()
visitors_schema = VisitorSchema(many=True)





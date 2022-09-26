from main import ma
from marshmallow.validate import Length

class AdminSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["admin_id", "username", "full_name", "email", "password", "shift"]
    password = ma.String(validate=Length(min=6, max=13))

# multiple schemas is not necessary right now, just the single schema for log in purposes
admin_schema = AdminSchema()
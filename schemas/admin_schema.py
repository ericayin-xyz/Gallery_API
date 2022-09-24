from main import ma
from marshmallow.validate import Length

class AdminSchema(ma.Schema):
    class Meta:
        fields = ("username", "email", "password")
    password = ma.String(validate=Length(min=6, max=13))

admin_schema = AdminSchema()
# multiple schemas is necessary right now
# admins_schema = AdminSchema(many=True)
from main import ma
from marshmallow import fields
from schemas.exhibition_schema import ExhibitionSchema
#create the Gallery Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class GallerySchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["gallery_id", "name", "phone_number", "location", "open_hours", "description", "exhibition"]
    exhibition = fields.Nested(ExhibitionSchema, only=("name", "start_date", "end_date",))

#single gallery schema
gallery_schema = GallerySchema()

#multiple gallery schema
gallerys_schema = GallerySchema(many=True)

from main import ma
from marshmallow import fields
#create the Gallery Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class GallerySchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["gallery_id", "name", "phone_number", "location", "open_hours", "description", "admin_id", "exhibition_id", "exhibitions"]
        load_only = ["gallery_id", "admin_id", "exhibition_id"]
    exhibitions = fields.List(fields.Nested("ExhibitionSchema", exclude = ("gallery", "artworks", "exhibition_id")))

#single gallery schema
gallery_schema = GallerySchema()
#multiple gallery schema
gallerys_schema = GallerySchema(many=True)

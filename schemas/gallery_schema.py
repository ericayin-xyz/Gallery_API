from main import ma

#create the Gallery Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class GallerySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "location", "phone_number", "open_hours", "description")

#single gallery schema
gallery_schema = GallerySchema()

#multiple gallery schema
gallerys_schema = GallerySchema(many=True)
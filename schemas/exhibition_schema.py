from main import ma
from marshmallow import fields

class ExhibitionSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["exihibition_id", "name", "start_date", "end_date", "artwork_id", "artwork"]
        load_only = ["artwork_id"]

    artwork = fields.Nested("ArtworkSchema", only=("title", "description",))
    # gallerys = fields.List(fields.Nested("GallerySchema", only = ("name","location",)))

exhibition_schema = ExhibitionSchema()
exhibitions_schema = ExhibitionSchema(many=True)

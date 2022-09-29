from main import ma
from marshmallow import fields

class ExhibitionSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["exhibition_id", "name", "start_date", "end_date", "artwork_id", "artworks", "gallery_id", "gallery"]
        load_only = ["exhibition_id", "artwork_id", "gallery_id"]
    artworks = fields.List(fields.Nested("ArtworkSchema", only=("title", "description",)))
    gallery = fields.Nested("GallerySchema", only = ("name", "location",))

exhibition_schema = ExhibitionSchema()
exhibitions_schema = ExhibitionSchema(many=True)

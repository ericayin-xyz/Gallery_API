from main import ma
from marshmallow import fields
from schemas.artwork_schema import ArtworkSchema

class ExhibitionSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["exihibition_id", "exihibition_name", "start_date", "end_date", "artwork_id", "artworks"]
        load_only = ["artwork_id"]
    artworks = fields.List(fields.Nested(ArtworkSchema, only=("title", "artist_id",)))

exhibition_schema = ExhibitionSchema()
exhibitions_schema = ExhibitionSchema(many=True)

from main import ma
from marshmallow import fields
from schemas.artwork_schema import ArtworkSchema

class ArtistSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["artist_id", "name", "dob", "biography", "artwork_id", "artworks"]

    artworks = fields.List(fields.Nested(ArtworkSchema, only=("title", "publish_date", "description",))) # exclude=("artist",) to avoid recursive calls between schemas

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)


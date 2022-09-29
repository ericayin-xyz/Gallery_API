from main import ma
from marshmallow import fields

class ArtworkSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["artwork_id", "title", "publish_date", "description", "artwork_type", "artwork_url", "artist_id", "artist", "exhibition_id", "exhibition"]
        load_only = ["artwork_id", "artist_id", "exhibition_id"]
    artist = fields.Nested("ArtistSchema", only=("name",))
    exhibition = fields.Nested("ExhibitionSchema", exclude = ("artworks",))

artwork_schema = ArtworkSchema()
artworks_schema = ArtworkSchema(many=True)


from main import ma
from marshmallow import fields

class ArtworkSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["artwork_id", "title", "publish_date", "description", "artwork_type", "artwork_url", "artist_id", "artists"]
        load_only = ['artist_id']
    # Schema is defined as a String , to avoid circular imports error
    artists = fields.Nested("ArtistSchema", only=("name", "start_date", "end_date"))

artwork_schema = ArtworkSchema()
artworks_schema = ArtworkSchema(many=True)


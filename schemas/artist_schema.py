from dataclasses import fields
from main import ma

class ArtistSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["artist_id", "name", "dob"]

artist_chema = ArtistSchema()
artists_schema = ArtistSchema(many=True)
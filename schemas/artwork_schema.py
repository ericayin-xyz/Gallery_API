from main import ma

class ArtworkSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["artwork_id", "title", "publish_date", "start_date", "end_date", "description", "artwork_type", "artwork_url", "artist_id"]

artwork_schema = ArtworkSchema()
artworks_schema = ArtworkSchema(many=True)


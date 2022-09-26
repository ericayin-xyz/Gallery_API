from main import ma

class ExhibitionSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["exihibition_id", "exihibition_name", "start_date", "end_date", "artwork_id"]

exhibition_schema = ExhibitionSchema()
exhibitions_schema = ExhibitionSchema(many=True)

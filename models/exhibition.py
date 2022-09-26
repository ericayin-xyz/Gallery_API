from main import db

class Exhibition(db.Model):
    __tablename__ = "exhibitions"
    exhibition_id = db.Column(db.Integer, primary_key=True)
    exhibition_name = db.Column(db.String(), default="colletion", nullable=False)
    start_date = db.Column(db.Date, db.ForeignKey("artworks.start_date"))
    end_date = db.Column(db.Date, db.ForeignKey("artworks.end_date"))
    artworks_id = db.Column(db.Integer, db.ForeignKey("artworks.artwork_id"), nullable=False)
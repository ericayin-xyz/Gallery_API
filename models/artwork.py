from main import db

class Artwork(db.Model):
    __tablename__ = "artworks"

    artwork_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    publish_date = db.Column(db.Date())
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    description = db.Column(db.String())
    artwork_type = db.Column(db.String())
    artwork_url = db.Column(db.String())
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.artist_id"))


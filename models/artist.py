from email.policy import default
from main import db

class Artist(db.Model):
    __tablename__ = "artists"

    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), default="Unknown")
    dob = db.Column(db.Date())  


    artworks = db.relationship(
        "Artwork",
        backref="artist"
    )
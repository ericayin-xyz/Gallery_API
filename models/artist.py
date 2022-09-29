from main import db

class Artist(db.Model):
    __tablename__ = 'artists'

    artist_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    dob = db.Column(db.Date()) 
    biography = db.Column(db.String()) 

    artworks = db.relationship(
        "Artwork",
        backref = "artist",
        cascade = "all, delete"
    )

from main import db

class Exhibition(db.Model):
    __tablename__ = 'exhibitions'

    exhibition_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable=False)
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())

    gallery_id = db.Column(db.Integer, db.ForeignKey("gallerys.gallery_id"), nullable=False)
    
    artworks = db.relationship(
        "Artwork",
        backref = "exhibition",
        cascade = "all, delete"
    )
    tickets = db.relationship(
        "Ticket",
        backref = "exhibition",
        cascade = "all, delete"
    )

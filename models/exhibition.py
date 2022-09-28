from main import db

class Exhibition(db.Model):
    __tablename__ = 'exhibitions'

    exhibition_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.artwork_id"), nullable=False)

    gallerys = db.relationship(
        "Gallery",
        backref = "exhibition",
        cascade = "all, delete"
    )
    tickets = db.relationship(
        "Ticket",
        backref = "exhibition",
        cascade = "all, delete"
    )

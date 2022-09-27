from main import db

class Ticket(db.Model):
    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True)
    entry_date = db.Column(db.Date(), nullable=False)
    entry_time = db.Column(db.String(), nullable=False)
    purchasing_time = db.Column(db.Date())

    visitor_id = db.Column(db.Integer, db.ForeignKey("visitors.visitor_id"), nullable=False)
    gallery_id = db.Column(db.Integer, db.ForeignKey("gallerys.gallery_id"), nullable=False)

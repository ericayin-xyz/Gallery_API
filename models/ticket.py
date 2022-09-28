from main import db
from datetime import date

class Ticket(db.Model):
    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True)
    entry_date = db.Column(db.Date(), nullable=False)
    entry_time = db.Column(db.String(), nullable=False)
    purchasing_date = db.Column(db.Date(), default = date.today())

    visitor_id = db.Column(db.Integer, db.ForeignKey("visitors.visitor_id"), nullable=False)
    gallery_id = db.Column(db.Integer, db.ForeignKey("gallerys.gallery_id"), nullable=False)
    exhibition_id = db.Column(db.Integer, db.ForeignKey("exhibitions.exhibition_id"), nullable=False)

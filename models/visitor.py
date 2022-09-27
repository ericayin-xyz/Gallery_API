import email
from main import db

class Visitor(db.Model):
    __tablename__ = 'visitors'
    
    # setting the columns
    visitor_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    tickets = db.relationship(
        "Ticket",
        backref = "visitor",
        cascade="all, delete"
    )



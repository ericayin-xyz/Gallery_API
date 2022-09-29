from main import db

class Gallery(db.Model):
    # define the table name in the database
    __tablename__ = 'gallerys'
    # Set the primary key
    gallery_id = db.Column(db.Integer, primary_key=True)
    # Add the rest of the attributes. 
    name = db.Column(db.String(), nullable=False, unique=True)
    location = db.Column(db.String())
    phone_number = db.Column(db.Integer())
    open_hours = db.Column(db.String())
    description = db.Column(db.String())
    
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.admin_id"), nullable=False)

    tickets = db.relationship(
        "Ticket",
        backref = "gallery",
        cascade = "all, delete"
    )
    exhibitions = db.relationship(
        "Exhibition",
        backref = "gallery",
        cascade = "all, delete"
    )
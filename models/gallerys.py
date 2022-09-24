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
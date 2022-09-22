from main import db

class Gallery(db.Model):
    # define the table name for the db
    __tablename__ = 'GALLERY'
    # Set the primary key
    id = db.Column(db.Integer, primary_key=True)
    # Add the rest of the attributes. 
    name = db.Column(db.String())
    location = db.Column(db.String())
    phone_number = db.Column(db.Integer())
    open_hours = db.Column(db.Integer())
    description = db.Column(db.String())
from main import db

class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    full_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)   
    shift = db.Column(db.String(), default= "Monday to Friday")

    gallerys = db.relationship(
        "Gallery",
        backref="admin",
        cascade="all, delete"
    )



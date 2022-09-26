from main import db
from flask import Blueprint
from main import bcrypt
from models.gallerys import Gallery
from models.visitors import Visitor
from models.admin import Admin

db_commands = Blueprint("db", __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Table created')

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Table dropped')

@db_commands.cli.command('seed')
def seed_db():

    admin1 = Admin(
        username = "YQ001",
        full_name = "Erika Y",
        email = "erika@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(admin1)

    visitor1 = Visitor(
        username = "Caby",
        email = "caby@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(visitor1)

    visitor2 = Visitor(
        username = "Lucy",
        email = "lucy@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(visitor2)

    visitor3 = Visitor(
        username = "Andy",
        email = "andy@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(visitor3)

    gallery1 = Gallery(
        name = "NSW Gallery",
        location = "NSW",
        phone_number = "042582931",
        open_hours = "10:00-17:00",
        description = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    db.session.add(gallery1)

    gallery2 = Gallery(
        name = "Mel Gallery",
        location = "MEL",
        phone_number = "042595664",
        open_hours = "10:00-17:00",
        description = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    db.session.add(gallery2)

    gallery3 = Gallery(
    name = "Canberra Gallery",
    location = "ACT",
    phone_number = "042596623",
    open_hours = "10:00-17:00",
    description = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    db.session.add(gallery3)

    db.session.commit()
    print("Table seeded")

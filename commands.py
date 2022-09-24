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
        email = "erika@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(admin1)

    gallery1 = Gallery(
        name = "NSW Gallery",
        location = "NSW",
        phone_number = "042582931",
        open_hours = "10",
        description = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    db.session.add(gallery1)

    db.session.commit()
    print("Table seeded")

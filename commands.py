from time import strftime
from main import db
from flask import Blueprint
from main import bcrypt
from models.gallery import Gallery
from models.visitor import Visitor
from models.admin import Admin
from models.artist import Artist
from models.artwork import Artwork
from models.exhibition import Exhibition
from models.ticket import Ticket
from datetime import date

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
    

    admin1 = Admin(
        username = "YQ001",
        full_name = "Erika Y",
        email = "erika@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(admin1)
    db.session.commit()
    
    artist1 = Artist(
        name = "Mzart",
        dob ="1800-12-01",
        biography = "Domenica dqwrq"
    )
    db.session.add(artist1)

    artist2 = Artist(
        name = "Domenica",
        dob ="1840-10-02",
        biography = "Domenica dqwrq"
    )
    db.session.add(artist2)   
    db.session.commit()

    artwork1 = Artwork(
        title = "Modern Music",
        publish_date = "2022-12-01",
        artwork_type = "modern",
        description = "ABCDEFGHIJKLMNOPQRST",
        artist = artist2
    )
    db.session.add(artwork1)

    artwork2 = Artwork(
        title = "Classic Pantings",
        publish_date = "2023-10-22",
        artwork_type = "modern",
        description = "ABCDEFGHIJKLMNOPQRST",
        # add the object, SQLAlchemy will handle it
        artist = artist1
    )
    db.session.add(artwork2)
    db.session.commit()

    exhibition1 = Exhibition(
        name = "Rabbit",
        start_date = "2023-04-22",
        end_date = "2023-06-22",
        artwork = artwork2
    )
    db.session.add(exhibition1)

    exhibition2 = Exhibition(
        name = "Rock",
        start_date = "2023-04-28",
        end_date = "2023-06-20",
        artwork = artwork2
    )
    db.session.add(exhibition2)
    db.session.commit()

    gallery1 = Gallery(
        name = "NSW Gallery",
        location = "NSW",
        phone_number = "042582931",
        open_hours = "10:00-17:00",
        description = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        exhibition = exhibition1,
        admin = admin1
    )
    db.session.add(gallery1)

    gallery2 = Gallery(
        name = "Mel Gallery",
        location = "MEL",
        phone_number = "042595664",
        open_hours = "10:00-17:00",
        description = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        exhibition = exhibition1,
        admin = admin1
    )
    db.session.add(gallery2)

    gallery3 = Gallery(
        name = "Canberra Gallery",
        location = "ACT",
        phone_number = "042596623",
        open_hours = "10:00-17:00",
        description = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        exhibition = exhibition1,
        admin = admin1
    )
    db.session.add(gallery3)
    db.session.commit()

    ticket1 = Ticket(
        entry_date = "2023-04-24",
        entry_time = "13:00",
        purchasing_date = date.today(),
        visitor = visitor1,
        gallery = gallery1,
        exhibition = exhibition2
    )
    db.session.add(ticket1)

    ticket2 = Ticket(
        entry_date = "2023-05-22",
        entry_time = "15:00",
        purchasing_date = date.today(),
        visitor = visitor2,
        gallery = gallery3,
        exhibition = exhibition1,
    )
    db.session.add(ticket2)

    db.session.commit()
    print("Table seeded")

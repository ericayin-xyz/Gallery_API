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
        username = "visitor1",
        email = "visitor1@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(visitor1)

    visitor2 = Visitor(
        username = "visitor2",
        email = "visitor2@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(visitor2)

    visitor3 = Visitor(
        username = "visitor3",
        email = "visitor3@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(visitor3)

    admin1 = Admin(
        username = "Luyue",
        full_name = "Luyue Yin",
        email = "admin1@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(admin1)

    admin2 = Admin(
        username = "Jairo",
        full_name = "Jairo Bilbao",
        email = "admin2@gmail.com",
        password = bcrypt.generate_password_hash("1234567").decode("utf8")
    )
    db.session.add(admin2)

    artist1 = Artist(
        name = "HE AN",
        dob ="1971-01-01",
        biography = "He An's work is autobiographic and obsessive, straddling the line between illegality and investigation and exploring the prohibitions and taboos of contemporary."
    )
    db.session.add(artist1)

    artist2 = Artist(
        name = "Daniel Boyd",
        dob ="1980-01-01",
        biography = "Daniel Boyd is considered one of Australia's leading artists. A Kudjala, Ghungalu, Wangerriburra, Wakka Wakka, Gubbi Gubbi, Kuku Yalanji, Bundjalung and Yuggera man with ni-Vanuatu heritage, he now lives and works on Gadigal/Wangal Country, Sydney. His work reinterprets Eurocentric perspectives on Australian history and the ethics of colonisation by drawing from historic photographs, art-historical references and his own personal and cultural history."
    )
    db.session.add(artist2)   

    artist3 = Artist(
        name = "Yujun C",
        dob ="1980-01-01",
        biography = "Chen works across diverse media and forms, including oil painting, collage and installation. His work has been shown in solo and group exhibitions within China and internationally, and was selected for the 55th Venice Biennale (2013) and the Shenzhen Sculpture Biennale."
    )
    db.session.add(artist3) 
    db.session.commit()

    gallery1 = Gallery(
        name = "White Rabbit Gallery",
        location = "30 Balfour St, Chippendale NSW 2008",
        phone_number = "0283992867",
        open_hours = "Wednesday to Sunday 10:00-17:00",
        description = "The White Rabbit Gallery is conveniently located a short 10 minute walk from Central and Redfern train stations and the Railway Square bus terminal. We don’t have parking spaces available, but there is limited on-street 2 hour metered parking in the area. Alternatively, Broadway Shopping Centre has a car park offering the first 2 hours free of charge, it is also a short 10 minute walk from the gallery.",
        admin = admin1
    )
    db.session.add(gallery1)

    gallery2 = Gallery(
        name = "Art Gallery of NSW",
        location = "Art Gallery Rd, Sydney NSW 2000",
        phone_number = "1800679278",
        open_hours = "10:00-17:00",
        description = "Visit on a Wednesday evening until 10pm for Art After Hours and see a slice of Sydney culture with free celebrity talks, music, performances, films and special events.Don't miss one of the free daily guided tours. Regular guided tours are offered in Japanese, Mandarin, Cantonese and Korean.",
        admin = admin1
    )
    db.session.add(gallery2)

    gallery3 = Gallery(
        name = "Brett Whiteley Studio",
        location = "2 Raper St, Surry Hills NSW 2010",
        phone_number = "0292251881",
        open_hours = "Thursday to Sunday, 10:00-16:00",
        description = "The Brett Whiteley Studio was the workplace and home of Australian artist, Brett Whiteley (1939-92). The artist bought the former warehouse in 1985 and converted it into a studio and exhibition space. He lived there from 1987 to 1992, the year he died in Thirroul.The visitor is offered the unique opportunity to experience the atmosphere of the space – the studio with his unfinished paintings, art equipment and collections of reference books, and the graffiti wall covered with quotes and images.",
        admin = admin1
    )
    db.session.add(gallery3)
    db.session.commit()

    exhibition1 = Exhibition(
        name = "I LOVE YOU",
        start_date = "2022-02-07",
        end_date = "2023-11-21",
        gallery_id = gallery1.gallery_id
    )
    db.session.add(exhibition1)

    exhibition2 = Exhibition(
        name = "Treasure Island",
        start_date = "2023-04-28",
        end_date = "2023-06-20",
        gallery_id = gallery2.gallery_id
    )
    db.session.add(exhibition2)
    db.session.commit()

    artwork1 = Artwork(
        title = "Daniel Boyd Untitled (DOC) 2016",
        publish_date = "2016-01-01",
        description = "Celebrate the interconnected histories of First Nations peoples through the works of Daniel Boyd",
        artist = artist2,
        exhibition = exhibition1
    )
    db.session.add(artwork1)

    artwork2 = Artwork(
        title = "Affinities and Resonances",
        publish_date = "2022-08-07",
        artwork_type = "20th-century American art",
        description = "Discover the affinities and resonances between one of the 20th century's most influential artists, Australian Central Desert painting, and contemporary American and Aboriginal musicians",
        # add the object, SQLAlchemy will handle it
        artist = artist1,
        exhibition = exhibition1
    )
    db.session.add(artwork2)

    artwork3 = Artwork(
        title = "Affinities and Resonances",
        publish_date = "2022-08-07",
        artwork_type = "International art",
        description = "The Art Gallery of NSW boasts a distinguished and extensive collection of British Victorian art, along with smaller but impressive holdings of Dutch, French and Italian painters of the 16th, 17th and 18th centuries, and an excellent collection of modern British masters and European modernists. Key names in art history are represented, from Peter Paul Rubens to Pablo Picasso.",
        # add the object, SQLAlchemy will handle it
        artist = artist2,
        exhibition = exhibition2
    )
    db.session.add(artwork3)
    db.session.commit()

    ticket1 = Ticket(
        entry_date = "2022-10-24",
        entry_time = "13:00",
        purchasing_date = date.today(),
        visitor = visitor1,
        gallery = gallery1,
        exhibition = exhibition2
    )
    db.session.add(ticket1)

    ticket2 = Ticket(
        entry_date = "2022-11-12",
        entry_time = "15:30",
        purchasing_date = date.today(),
        visitor = visitor2,
        gallery = gallery3,
        exhibition = exhibition1,
    )
    db.session.add(ticket2)

    db.session.commit()
    print("Table seeded")

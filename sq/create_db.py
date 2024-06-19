from flask import Flask
from models import Artist, Album, Song, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # создаем тестовых исполнителей
        artist1 = Artist(name='YUNGBLUD')
        artist2 = Artist(name='Em Beihold')
        artist3 = Artist(name='Takayan')
        db.session.add_all([artist1, artist2, artist3])
        db.session.commit()

        # создаем тестовые альбомы
        album1 = Album(title='Weird!', year='2020', artist=artist1)
        album2 = Album(title='21st Century Liability', year='2018', artist=artist1)
        album3 = Album(title='Egg in the Backseat', year='2022', artist=artist2)
        album4 = Album(title='City of Angels', year='2020', artist=artist2)
        album5 = Album(title='Happiness and correct answer', year='2020', artist=artist3)
        album6 = Album(title='Lateralus', year='2001', artist=artist3) 
        album7 = Album(title='AEnima', year='1996', artist=artist3) 
        album8 = Album(title='10,000 Days', year='2006', artist=artist3) 

        # создаем тестовые песни
        song1 = Song(title='cotton candy', length='2:47', track_number=3, album=album1)
        song2 = Song(title='parents', length='2:51', track_number=2, album=album1)
        song3 = Song(title='Machine Gun', length='3:13', track_number=5, album=album2)
        song4 = Song(title='Medication', length='3:12', track_number=4, album=album2)
        song5 = Song(title='Numb Little Bug', length='2:49', track_number=2, album=album3)
        song6 = Song(title='City of Angels', length='3:14', track_number=7, album=album4)
        song7 = Song(title='Toy', length='3:17', track_number=3, album=album5)
        song8 = Song(title='Just disappear', length='2:47', track_number=5, album=album5)
        db.session.add_all([album1, album2, album3, album4, album5, album6, album7, album8, song1, song2, song3, song4, song5, song6, song7, song8])
        db.session.commit()
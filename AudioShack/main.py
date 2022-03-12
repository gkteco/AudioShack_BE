from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
main.config["UPLOAD_FOLDER"] = "static/"

db = SQLAlchemy(main)

#models for storing JSON objects

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    mp3 = db.Column(db.LargeBinary)

    album_art_id = db.Column(db.String, db.ForeignKey('album_art.image'))
    album_art = db.relationship('Album_art', backref=db.backref('songs'))

    genre_id = db.Column(db.String, db.ForeignKey('genre.genre_name'))
    genre = db.relationship('Genre', backref=db.backref('songs'))

    artist_id = db.Column(db.String, db.ForeignKey('artist.artist_name'))
    artist = db.relationship('Artist', backref=db.backref('songs'))

    def __repr__(self):
        return 'Song Title: ' % self.title

    def __init__(self, title, album_art, genere, artist):
        self.title = title
        self.mp3 = mp3
        self.album_art = album_art
        self.genre = genre
        self.artist = artist

class Album_art(db.Model):
    art_name = db.Column(db.String, primary_key = True)
    image = db.Column(db.LargeBinary)

class Genre(db.Model):
    genre_name = db.Column(db.String, primary_key = True)

class Artist(db.Model):
    artist_name = db.Column(db.String, primary_key = True)
    profile_pic = db.Column(db.String)

db.create_all()

#API CONFIG

from marshmallow_jsonapi import Schema, fields

class SongSchema(Schema):
    class Meta:
        type_ ='song'
        self_view = 'song_one'
        self_view_kwargs = {'title': '<title>'}
        self_view_many = 'song_all'

    id = fields.Integer()
    title = fields.String()
    mp3 = fields.LargeBinary()
    album_art_id = fields.Url()
    genre_id = fields.String()
    artist_id = fields.String()

from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

class SongMany(ResourceList):
    schema = SongSchema
    data_layer = {
            "session": db.session,
            "model": Song
    }

class SongOne(ResourceDetail):
    schema = SongSchema
    data_layers = {
            'session': db.session,
            'model': Song
    }


api = Api(main)
api.route(SongMany, 'song_all', '/data/songs')
api.route(SongOne, 'song_one', '/song/<int:title>')


from twilio.rest import Client
from werkzeug.utils import secure_filename

# API routes
@main.route('/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(main.config['UPLOAD_FOLDER'] + filename)
        return f'Uploaded: {file.filename}'
    title = request.form['title']
    album_art_id = request.form['album_art_id']
    genre_id = request.form['genre_id']
    artist_id = request.form['artist_id']
    song = Song(title, album_art_id, genre_id, artist_id)
    db.session.add(song)
    db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    main.run(debug=True)



















































# AudioShack_BE
Backend for AudioShack, a blockchain application that will help musicians manage their music.


[End Point Docs]

'/' = request to upload song (title, mp3,  album_art, genre, artist)

'/data/songs' = get all songs 

'/song/<int:title>' = get one song

[How To Use]

make sure to install latest python

1) git clone git@github.com:giannicrivello/AudioShack_BE.git
2) cd AudioShack_BE
3) source env/bin/activate
4) pip install -r requirements.txt
5) cd AudioShack
6) python3 main.py

server will be listening on http://localhost:5000

[example endpoint]
'http://localhost:5000/' = request to upload song
'http://localhost:5000/data/songs' = get all songs
'http://localhost:5000/song/<int:title>' = get one song


# music_routes.py
from flask import render_template
from flask_login import login_required
from models import Song
from app import app

@app.route('/afroworld')
def afroworld():
    return render_template('afroworld.html')

@app.route('/afroworld/playlist')
@login_required
def playlist():
    # Fetch songs from the database or any other logic
    songs = Song.query.all()
    return render_template('playlist.html', songs=songs)

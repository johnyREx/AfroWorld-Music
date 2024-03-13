# routes.py
from flask import render_template
from flask_login import login_required
from models import Song

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/play/<int:song_id>')
@login_required
def play_song(song_id):
    # Fetch song from database based on song_id
    song = Song.query.get_or_404(song_id)
    return render_template('music_player.html', song=song)


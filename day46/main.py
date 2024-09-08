import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
date=input("What year do you want to travel to?Type the date in this format YYYY-MM-DD:")
URL=f"https://www.billboard.com/charts/hot-100/{date}/"
response=requests.get(URL)
data=response.text
soup=BeautifulSoup(data,"html.parser")
song_names_spans=soup.select("li ul li h3")
song_names=[song.getText().strip()for song in song_names_spans]




sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public",client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,show_dialog=True,
        cache_path="token.txt"
                                               ))
user_id = sp.current_user()["id"]
print(user_id)
# Create a new playlis
playlist=sp.user_playlist_create(user=user_id,name=f"Top 100 for the year{date}",collaborative=False,description="HAHA MY APP CREATED THIS PLAYLIST")
# Search for each song on Spotify and add to the playlist
playlist_id=playlist["id"]
for i in song_names:
    print(i)
    results = sp.search(q=i, type="track",limit=1)
    tracks=results["tracks"]["items"]
    track = tracks[0]
    track_id = track['id']
    sp.playlist_add_items(playlist_id, [track_id])
    #sp.user_playlist_add_tracks(user_id, playlist_id, results, position=None)
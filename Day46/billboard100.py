import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://www.google.com/",
                                               scope="playlist-modify-private user-read-private"))
user_id = sp.current_user()["id"]

url = "https://ca.billboard.com/charts/hot-100/2025-11-22"


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, "html.parser")

h2_tags = soup.find_all(name="h2", class_="chart-item-headline")
song_list = [tag.getText() for tag in h2_tags]

song_uri_list = []
for song in song_list:
    result = sp.search(q=song, type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uri_list)

playlist = sp.current_user_playlist_create(
    name="November 22, 2025 Billboard 100 Playlist",
    public=False
)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uri_list
)
import base64
import requests
import random
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


def get_spotify_access_token():
    url = "https://accounts.spotify.com/api/token"
    client_creds = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

    headers = {
        "Authorization": f"Basic {client_creds_b64}",
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get access token: {response.status_code}, {response.text}")


def get_playlist(mood):
    mood_queries = {
        "Very Happy": ["party anthems", "high energy pop", "festival hits", "dance party", "feel-good pop"],
        "Happy": ["summer vibes", "good vibes", "happy indie", "positive energy"],
        "Neutral": ["lo-fi beats", "ambient chill", "chill instrumental", "focus mode"],
        "Slightly Sad": ["mellow acoustic", "sad indie", "soft piano"],
        "Very Sad": ["sad ballads", "broken heart songs", "soft rock", "lonely nights", "emotional hits"]
    }

    mood = mood.title()
    if mood not in mood_queries:
        mood = "Neutral"

    search_query = random.choice(mood_queries[mood])

    access_token = get_spotify_access_token()
    search_url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {
        "q": search_query,
        "type": "playlist",
        "limit": 5
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        playlists = []
        while not playlists:
            for playlist in response.json()["playlists"]["items"]:
                if playlist:
                    playlists.append({
                        "name": playlist["name"],
                        "url": playlist["external_urls"]["spotify"],
                        "image": playlist["images"][0]["url"] if playlist["images"] else None  # Get the first image
                    })
        return playlists
    else:
        raise Exception(f"Failed to fetch playlists: {response.status_code}, {response.text}")

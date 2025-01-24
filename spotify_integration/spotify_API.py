import base64
import requests
from sentiment_analysis.analyze import user_mood
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


def get_spotify_access_token():

    url = "https://accounts.spotify.com/api/token"

    client_creds = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

    headers = {
        "Authorization": f"Basic {client_creds_b64}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get access token: {response.status_code}, {response.text}")


def get_playlist():

    mood = user_mood()

    mood_to_search_query = {
        "Very Happy": "high energy party hits",
        "Happy": "chill vibes",
        "Neutral": "lo-fi beats",
        "Slightly Sad": "mellow acoustic",
        "Very Sad": "soft ballads"
    }

    playlist_query = mood_to_search_query.get(mood, "chill vibes")

    access_token = get_spotify_access_token()

    # Define the search endpoint and parameters
    search_url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "q": playlist_query,
        "type": "playlist",
        "limit": 5
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        playlists = []
        for playlist in response.json()["playlists"]["items"]:
            playlists.append({
                "name": playlist["name"],
                "url": playlist["external_urls"]["spotify"]
            })
        return playlists
    else:
        raise Exception(f"Failed to fetch playlists: {response.status_code}, {response.text}")

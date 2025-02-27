from flask import Flask, request, jsonify, render_template
from spotify_integration.spotify_API import get_playlist
from sentiment_analysis.analyze import user_mood

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_playlist", methods=["POST"])
def get_playlist_route():
    data = request.get_json()
    mood = data.get("mood")
    mood_of_user = user_mood(mood)

    try:
        playlists = get_playlist(mood_of_user)
        print(f"Fetched playlists: {playlists}")
        return jsonify(playlists=playlists)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True)

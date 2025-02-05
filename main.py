from spotify_integration.spotify_API import get_playlist

print("🎵 Welcome to Moodify! 🎵")
print("Let your mood guide your music experience!\n")

try:
    playlists = get_playlist()

    print("\n✨ Recommended Playlists for You ✨")
    for idx, playlist in enumerate(playlists):
        print(f"{idx+1}. {playlist['name']} - {playlist['url']}")

except Exception as e:
    print("\n❌ Oops! Something went wrong.")
    print(f"Error: {e}")

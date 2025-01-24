from spotify_integration.spotify_API import get_playlist


print("🎵 Welcome to Moodify! 🎵")
print("Let your mood guide your music experience!\n")

try:
    # Get playlists based on the user's mood
    playlists = get_playlist()

    # Display the playlists
    print("\n✨ Recommended Playlists for You ✨")
    for idx, playlist in enumerate(playlists, start=1):
        print(f"{idx}. {playlist['name']} - {playlist['url']}")

except Exception as e:
    print("\n❌ Oops! Something went wrong.")
    print(f"Error: {e}")
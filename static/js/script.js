function getPlaylist() {
    let mood = document.getElementById("moodInput").value.trim();

    if (mood === "") {
        alert("Please enter a mood! 🎭");
        return;
    }

    // Fun loading messages
    let funnyMessages = [
        "🎶 Finding the perfect playlist... Hold on to your headphones!",
        "🎧 Scanning the Spotify universe for good vibes...",
        "🎵 Mixing beats and matching moods... Almost there!"
    ];
    let randomMessage = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];

    // Show loading text
    document.getElementById("funny-text").innerText = randomMessage;

    fetch("/get_playlist", {
        method: "POST",
        body: JSON.stringify({ mood: mood }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `<h2>🎵 Here’s Your Playlist:</h2>`;

        data.playlists.forEach(playlist => {
            let playlistElement = document.createElement("p");
            playlistElement.innerHTML = `<a href="${playlist.url}" target="_blank">${playlist.name} 🔗</a>`;
            resultDiv.appendChild(playlistElement);
        });

        // Remove loading message
        document.getElementById("funny-text").innerText = "";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("funny-text").innerText = "🚨 Oops! Something went wrong. Try again!";
    });
}

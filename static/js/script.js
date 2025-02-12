async function getPlaylist() {
    // Get the user's mood
    const mood = document.getElementById("moodInput").value;

    if (!mood) {
        document.getElementById("result").innerHTML = "<p>Please enter your mood!</p>";
        return;
    }

    // Send the mood to the backend via a POST request
    try {
        const response = await fetch('/get_playlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ mood: mood }),
        });

        // Parse the JSON response
        const data = await response.json();

        // Display the result
        if (data.error) {
            document.getElementById("result").innerHTML = `<p>${data.error}</p>`;
        } else if (data.playlists) {
            let playlistsHtml = '<h2>Recommended Playlists:</h2><ul>';
            data.playlists.forEach(playlist => {
                playlistsHtml += `<li><a href="${playlist.url}" target="_blank">${playlist.name}</a></li>`;
            });
            playlistsHtml += '</ul>';
            document.getElementById("result").innerHTML = playlistsHtml;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById("result").innerHTML = "<p>Something went wrong. Please try again later.</p>";
    }
}

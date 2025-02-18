async function getPlaylist() {
    const mood = document.getElementById("moodInput").value;

    if (!mood) {
        document.getElementById("result").innerHTML = "<p>Please enter your mood!</p>";
        return;
    }

    try {
        const response = await fetch('/get_playlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ mood: mood }),
        });

        const data = await response.json();

        if (data.error) {
            document.getElementById("result").innerHTML = `<p>${data.error}</p>`;
        } else if (data.playlists) {
            let playlistsHtml = '<h2>Recommended Playlists:</h2><div class="playlist-container">';
            data.playlists.forEach(playlist => {
                playlistsHtml += `
                    <div class="playlist-card">
                        <img src="${playlist.image}" alt="Playlist Image" class="playlist-image">
                        <a href="${playlist.url}" target="_blank">${playlist.name}</a>
                    </div>
                `;
            });
            playlistsHtml += '</div>';
            document.getElementById("result").innerHTML = playlistsHtml;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById("result").innerHTML = "<p>Something went wrong. Please try again later.</p>";
    }
}

import requests
import config

class SpotifyRequests:
    playlist_ids = {'Ontdekkingen': '6RierTdc8hHZO7uruDkaGB'}

    def get_playlist_tracks(self, playlist):
        headers = {
            'Authorization': f"Bearer {config.SPOTIFY_TOKEN}",
        }
        tracks = requests.get(
            f"https://api.spotify.com/v1/playlists/{self.playlist_ids[playlist]}/tracks",
            headers=headers).json()

        return(tracks)




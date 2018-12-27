import requests
import config
import csv

class PlaylistTracks:
    playlist_ids = {'Ontdekkingen': '6RierTdc8hHZO7uruDkaGB'}

    def get_playlist_tracks(self, playlist):
        headers = {
            'Authorization': f"Bearer {config.SPOTIFY_TOKEN}",
        }
        self.tracks = requests.get(
            f"https://api.spotify.com/v1/playlists/{self.playlist_ids[playlist]}/tracks",
            headers=headers)

    def save_relevant_album_fields(self):
        outputFile = open('data/albums_to_buy.csv', 'w')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(['artist', 'album'])

        for track in self.tracks.json()['items']:
            artist = track['track']['artists'][0]['name']
            album = track['track']['album']['name']
            outputWriter.writerow([artist, album])

        outputFile.close()






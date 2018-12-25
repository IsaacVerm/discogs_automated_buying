from lib.spotify_requests import SpotifyRequests

if __name__ == "__main__":
    tracks = SpotifyRequests().get_playlist_tracks('Ontdekkingen')
    print(tracks)

from lib.playlist_tracks import PlaylistTracks

if __name__ == "__main__":
    tracks = PlaylistTracks()
    tracks.get_playlist_tracks('Ontdekkingen')
    tracks.save_relevant_album_fields()

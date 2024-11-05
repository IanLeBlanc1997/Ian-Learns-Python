import requests 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
class SpotifyClient:
    def __init__(self):
        spotify_id = '14359fb92f81494c912a2607827d8bf8'
        spotify_secret = 'ff9e0aded6a543e4a74b2c7f0de505a3' 
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                username='leblania',
                                cache_path='token.txt',
                                show_dialog=True,
                                scope='playlist-modify-private',
                                client_id=spotify_id,
                                client_secret=spotify_secret,
                                redirect_uri='https://example.com'))  #the documentation was wrong and lame on this one
        self.user_id = self.sp.current_user()['id'] 
        
    def make_playlist(self,billboard_data,date):
        uris = []
        for song,artist in billboard_data.items(): #run through the tracklist 
            track = self.sp.search(q=f"track: {song} artist: {artist}",type='track') #the documentation was kind of lame on this one too
            try:
                uri = track['tracks']['items'][0]['uri'] #this index is apparently correct but it doesn't always come up with the right track
                uris.append(uri)
            except:
                print(f"{track} not found on spotify- skipped")

        playlist = self.sp.user_playlist_create(name=f'{date} Billboard Top 100',user=self.user_id,public=False) #create playlist
        playlist_id = playlist['id']
        self.sp.user_playlist_add_tracks(user=self.user_id,playlist_id=playlist_id,tracks=uris) #add to playlist
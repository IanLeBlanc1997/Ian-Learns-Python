import requests 
from bs4 import BeautifulSoup
class BillboardScraper:
    def __init__(self):
        pass
    def scrape(self,date):
        headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15'}
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/",headers=headers)
        data = response.text
        soup = BeautifulSoup(data,'html.parser')
        songs = soup.select('li ul li h3')
        artists = soup.select('li ul li span')
        artists = [artist.getText() for artist in artists]
        artists = [artist.strip() for artist in artists]
        artists= [artist for artist in artists if not artist.isdigit()] # learned about the isdigit() method and the isinstance method to check for type
        artists= [artist for artist in artists if not artist == "-"]
        songs = [song.getText() for song in songs]
        songs = [song.strip() for song in songs]
        songs_and_artists = dict(zip(songs,artists)) #learned the dict() function which makes a dictionary and the zip() function which unzips iterables and turns them to tuples
        return songs_and_artists
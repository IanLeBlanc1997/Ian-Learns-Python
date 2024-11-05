import requests
from bs4 import BeautifulSoup
from billboard_scraper import BillboardScraper
from spotify_client import SpotifyClient
date = input("Enter a date in the past to make a playlist from!\nMust be in YYYY-MM-DD format\n")
# date = '1997-02-02'
year = int(date.split('-')[0])
scraper = BillboardScraper()
billboard_data = scraper.scrape(date)
playlist_maker = SpotifyClient()
playlist_maker.make_playlist(billboard_data=billboard_data,date=date)


from webscraper import webscrape
from form_filler import fill_form
import time
addresses,rents,urls = webscrape()
fill_form(addresses,rents,urls)
from bs4 import BeautifulSoup
import requests
import re

def webscrape():
    response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    addresses = soup.findAll(name='address')
    addresses = [address.getText().strip() for address in addresses]
    rents = soup.findAll(name= 'span', class_="PropertyCardWrapper__StyledPriceLine")
    rents = [rent.getText().strip() for rent in rents]
    rents = [re.split(r'\+|/', rent)[0] for rent in rents]
    urls = soup.findAll(name='a',class_="StyledPropertyCardDataArea-anchor")
    test = soup.find(name='a',class_="StyledPropertyCardDataArea-anchor")
    urls = [url['href'] for url in urls]
    return addresses,rents,urls


import requests 
from bs4 import BeautifulSoup
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data,"html.parser")
titles = [movie.getText().split(" ",maxsplit=1)[1] for movie in soup.select("h3")]
titles.reverse()
print(titles)
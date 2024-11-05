from bs4 import BeautifulSoup
with open('day_45_web_scraping/bs4-start/website.html') as website:
    contents = website.read()

soup = BeautifulSoup(contents,'html.parser')
# print(soup.title) 
# print(soup.title.string) #find specific titles and search title attributes

all_anchor_tags = soup.find_all(name='a') #find all of a certain tag

for tag in all_anchor_tags:
    print(tag.getText())     # go through all of the tags and pull a certain attribute of those tags out

for tag in all_anchor_tags:
    print(tag.get("href"))   #search for a specific attribute name

heading = soup.find(name='h1',id='name') #the find function creates a python object
        # in this case, we search for the first object with the name <h1> AND the <h1> with the id 'name'
print(heading)

books_and_teach = soup.find(name='h3',class_='heading') #we can do the same thing with the class attribute, use the key "class_"
print(books_and_teach)

company_url = soup.select_one(selector= 'p a') #use the select one to select specific tag embedding of items in the html
print(company_url)

name = soup.select_one(selector = "#name") #we can do the same thing for selecting for ID using the #

headings = soup.select(selector=".heading") # or similarly search for classes. The select method will return a list of every tag with that class

print(headings)



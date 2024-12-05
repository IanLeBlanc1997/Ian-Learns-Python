from flask import Flask, render_template
import dotenv
import random
from datetime import datetime
import requests
dotenv.load_dotenv()

app = Flask(__name__)

@app.route("/")
def homepage():
    random_number = random.randint(1,10)
    year = datetime.now().year
    return render_template('index.html', num=random_number,year=year)

@app.route("/<name>")
def name_guess(name):
    entry = name.capitalize()
    parameters = {'name':entry}
    genderize_response = requests.get('https://api.genderize.io',params=parameters)
    agify_response = requests.get('https://api.agify.io',params=parameters)
    age_data = agify_response.json()
    age= age_data['age']
    gender_data = genderize_response.json()
    gender = gender_data['gender']
    year = datetime.now().year
    return render_template('name_guess.html',year=year,age=age,gender=gender,name=entry)

@app.route("/blog/<num>")
def blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template('blog.html',posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
    